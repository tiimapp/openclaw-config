#!/usr/bin/env python3
"""
OpenClaw Config Backup Script
Backs up configuration files to a git repository with secret sanitization.
"""

import json
import logging
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set

# Configuration
SOURCE_DIR = Path.home() / ".openclaw"
BACKUP_DIR = Path.home() / "openclaw-config-backup"
LOG_FILE = BACKUP_DIR / "backup.log"

# Secrets to sanitize (key paths in JSON)
SENSITIVE_KEYS: Set[str] = {
    "apiKey",
    "token",
    "auth",
    "password",
    "secret",
}

# Files to backup
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
    
    # File handler
    fh = logging.FileHandler(LOG_FILE)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger


def sanitize_value(key: str, value) -> str:
    """Sanitize sensitive values."""
    if isinstance(value, str) and any(sk in key.lower() for sk in SENSITIVE_KEYS):
        return f"<${key.upper()}>"
    return value


def sanitize_config(data, parent_key: str = "") -> dict:
    """Recursively sanitize config dictionary."""
    if not isinstance(data, dict):
        return data
    
    sanitized = {}
    for key, value in data.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        
        if any(sk in key.lower() for sk in SENSITIVE_KEYS):
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
            shutil.copy2(src, dest)
        
        logger.info(f"Backed up: {src_name} -> {dest_path}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to backup {src_name}: {e}")
        return False


def backup_workspace(logger: logging.Logger) -> bool:
    """Backup workspace markdown files (excluding .git)."""
    src = SOURCE_DIR / "workspace"
    dest = BACKUP_DIR / "workspace"
    
    if not src.exists():
        logger.warning("Workspace directory not found")
        return False
    
    try:
        if dest.exists():
            shutil.rmtree(dest)
        
        # Copy tree but ignore .git directories
        def ignore_git(dir, contents):
            return ['.git'] if '.git' in contents else []
        
        shutil.copytree(src, dest, ignore=ignore_git)
        logger.info("Backed up: workspace/")
        return True
    except Exception as e:
        logger.error(f"Failed to backup workspace: {e}")
        return False


def git_commit(logger: logging.Logger) -> bool:
    """Commit changes to git repository."""
    try:
        # Add all changes first
        subprocess.run(
            ["git", "add", "."],
            cwd=BACKUP_DIR,
            check=True,
            capture_output=True
        )
        
        # Check if there are changes to commit
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=BACKUP_DIR,
            capture_output=True
        )
        
        if result.returncode == 0:
            logger.info("No changes to commit")
            return True
        
        # Commit
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(
            ["git", "commit", "-m", f"Backup: {timestamp}"],
            cwd=BACKUP_DIR,
            check=True,
            capture_output=True
        )
        
        logger.info(f"Committed changes at {timestamp}")
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
    
    changed = False
    
    # Backup config files
    for src, dest in FILES_TO_BACKUP.items():
        if backup_file(src, dest, logger):
            changed = True
    
    # Backup workspace
    if backup_workspace(logger):
        changed = True
    
    # Git commit if changes detected
    if changed:
        git_commit(logger)
    
    logger.info("Backup completed")
    return 0 if changed else 1


if __name__ == "__main__":
    sys.exit(main())
