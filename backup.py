#!/usr/bin/env python3
"""
OpenClaw Config Backup Script
Backs up configuration files to a git repository with secret sanitization.
NOTE: Workspace is excluded (too large for hourly config backup).
"""

import json
import logging
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Set

# Configuration
SOURCE_DIR = Path.home() / ".openclaw"
BACKUP_DIR = Path.home() / "openclaw-config-backup"
LOG_FILE = BACKUP_DIR / "backup.log"
GITHUB_REPO = "https://github.com/tiimapp/openclaw-config"

# Secrets to sanitize (exact key matches only)
SENSITIVE_KEYS: Set[str] = {
    "apiKey",
    "token",
    "auth",
    "password",
}

# Keys that should NEVER be sanitized (config settings, not secrets)
CONFIG_KEYS: Set[str] = {
    "maxTokens",
    "contextWindow",
    "cost",
    "input",
    "output",
}

# Files to backup (workspace excluded - too large for config backup)
FILES_TO_BACKUP = {
    "openclaw.json": "config/openclaw.json",
    "cron/jobs.json": "cron/jobs.json",
}


def setup_logging() -> logging.Logger:
    """Configure structured logging."""
    logger = logging.getLogger("openclaw_backup")
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    fh = logging.FileHandler(LOG_FILE)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger


def sanitize_config(data, parent_key: str = "") -> dict:
    """Recursively sanitize config dictionary."""
    if not isinstance(data, dict):
        return data
    
    sanitized = {}
    for key, value in data.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        
        if key in CONFIG_KEYS:
            sanitized[key] = value
        elif key in SENSITIVE_KEYS:
            sanitized[key] = f"<${key.upper()}>"
        elif isinstance(value, dict):
            sanitized[key] = sanitize_config(value, full_key)
        elif isinstance(value, list):
            sanitized[key] = [
                sanitize_config(item, full_key) if isinstance(item, dict) else item
                for item in value
            ]
        else:
            sanitized[key] = value
    
    return sanitized


def backup_file(src_name: str, dest_path: str, logger: logging.Logger) -> bool:
    """Backup a single file with sanitization."""
    src = SOURCE_DIR / src_name
    dest = BACKUP_DIR / dest_path
    
    if not src.exists():
        logger.warning(f"Source file not found: {src}")
        return False
    
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        
        if src_name.endswith('.json'):
            with open(src, 'r') as f:
                data = json.load(f)
            
            sanitized = sanitize_config(data)
            
            with open(dest, 'w') as f:
                json.dump(sanitized, f, indent=2)
        else:
            import shutil
            shutil.copy2(src, dest)
        
        logger.info(f"Backed up: {src_name} -> {dest_path}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to backup {src_name}: {e}")
        return False


def git_setup_remote(logger: logging.Logger) -> bool:
    """Setup GitHub remote if not already configured."""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=BACKUP_DIR,
            capture_output=True
        )
        
        if result.returncode != 0:
            subprocess.run(
                ["git", "remote", "add", "origin", GITHUB_REPO],
                cwd=BACKUP_DIR,
                check=True,
                capture_output=True
            )
            logger.info(f"Added GitHub remote: {GITHUB_REPO}")
        else:
            logger.info("GitHub remote already configured")
        
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to setup remote: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during remote setup: {e}")
        return False


def git_push(logger: logging.Logger) -> bool:
    """Push commits to GitHub."""
    try:
        subprocess.run(
            ["git", "push", "-u", "origin", "master"],
            cwd=BACKUP_DIR,
            check=True,
            capture_output=True,
            timeout=120
        )
        logger.info("Pushed to GitHub successfully")
        return True
        
    except subprocess.TimeoutExpired:
        logger.error("Git push timed out")
        return False
    except subprocess.CalledProcessError as e:
        logger.error(f"Git push failed: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during git push: {e}")
        return False


def git_commit(logger: logging.Logger, push_to_github: bool = False) -> bool:
    """Commit changes to git repository."""
    try:
        subprocess.run(
            ["git", "add", "."],
            cwd=BACKUP_DIR,
            check=True,
            capture_output=True
        )
        
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=BACKUP_DIR,
            capture_output=True
        )
        
        if result.returncode == 0:
            logger.info("No changes to commit")
            if push_to_github:
                git_push(logger)
            return True
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(
            ["git", "commit", "-m", f"Backup: {timestamp}"],
            cwd=BACKUP_DIR,
            check=True,
            capture_output=True
        )
        
        logger.info(f"Committed changes at {timestamp}")
        
        if push_to_github:
            git_push(logger)
        
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"Git operation failed: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during git commit: {e}")
        return False


def main():
    """Main backup orchestrator."""
    logger = setup_logging()
    logger.info("Starting OpenClaw config backup")
    
    git_setup_remote(logger)
    
    changed = False
    
    # Backup config files only (workspace excluded - too large)
    for src, dest in FILES_TO_BACKUP.items():
        if backup_file(src, dest, logger):
            changed = True
    
    if changed:
        git_commit(logger, push_to_github=True)
    else:
        git_push(logger)
    
    logger.info("Backup completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
