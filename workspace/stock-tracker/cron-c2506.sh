#!/bin/bash
#
# C2506 Corn Futures Monitor - Cron Job Script
#
# This script is called by cron to run the C2506 monitor.
# It auto-detects whether it's trading time and chooses the appropriate report type.
#
# Installation:
#   1. Make executable: chmod +x cron-c2506.sh
#   2. Add to crontab (see cron entries below)
#
# Cron Schedule:
#   During trading hours (hourly): 0 9,10,11,14,15 * * 1-5
#   Daily summary (after close):   30 15 * * 1-5
#

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="${SCRIPT_DIR}/c2506_monitor.py"
CONFIG_FILE="${SCRIPT_DIR}/c2506_config.json"
LOG_DIR="${SCRIPT_DIR}/logs"
LOG_FILE="${LOG_DIR}/c2506_cron.log"

# Create log directory if it doesn't exist
mkdir -p "${LOG_DIR}"

# Logging function
log() {
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[${timestamp}] $*" | tee -a "${LOG_FILE}"
}

# Error handling
error_exit() {
    log "ERROR: $*"
    exit 1
}

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    error_exit "Python3 is not installed or not in PATH"
fi

# Check if the monitor script exists
if [ ! -f "${PYTHON_SCRIPT}" ]; then
    error_exit "Monitor script not found: ${PYTHON_SCRIPT}"
fi

log "Starting C2506 monitor cron job"
log "Script: ${PYTHON_SCRIPT}"
log "Config: ${CONFIG_FILE}"

# Determine the mode based on when cron triggered this
# Cron passes the schedule, but we can also check trading time
CURRENT_HOUR=$(date '+%H')
CURRENT_MINUTE=$(date '+%M')
CURRENT_DAY=$(date '+%u')  # 1=Monday, 7=Sunday

log "Current time: $(date '+%Y-%m-%d %H:%M:%S') (Day of week: ${CURRENT_DAY})"

# Determine mode based on cron schedule
# If minute is 30, it's the daily summary (15:30)
# Otherwise, it's an hourly report during trading hours
if [ "${CURRENT_MINUTE}" = "30" ]; then
    MODE="daily"
    log "Mode: Daily summary (market close report)"
else
    MODE="hourly"
    log "Mode: Hourly report (during trading hours)"
fi

# Check if it's a weekday (1-5)
if [ "${CURRENT_DAY}" -gt 5 ]; then
    log "WARNING: Running on weekend (day ${CURRENT_DAY}). This should not happen based on cron schedule."
fi

# Run the monitor
log "Executing monitor with mode: ${MODE}"

cd "${SCRIPT_DIR}"

# Run Python script with appropriate mode
if python3 "${PYTHON_SCRIPT}" --mode "${MODE}" --config "${CONFIG_FILE}" >> "${LOG_FILE}" 2>&1; then
    log "Monitor completed successfully"
else
    EXIT_CODE=$?
    log "Monitor failed with exit code: ${EXIT_CODE}"
    exit ${EXIT_CODE}
fi

log "Cron job finished"
