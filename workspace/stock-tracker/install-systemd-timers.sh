#!/bin/bash
#
# Install C2506 Monitor systemd timers
#
# This script installs the systemd service and timer units for the C2506 monitor.
# Run with sudo privileges.
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYSTEMD_DIR="/etc/systemd/system"

echo "C2506 Monitor - Systemd Timer Installation"
echo "==========================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Error: This script must be run as root (use sudo)"
    exit 1
fi

# Check if systemd is available
if ! command -v systemctl &> /dev/null; then
    echo "Error: systemctl not found. systemd may not be available."
    exit 1
fi

echo "Installing service and timer units..."

# Copy service files
cp "${SCRIPT_DIR}/c2506-monitor.service" "${SYSTEMD_DIR}/"
cp "${SCRIPT_DIR}/c2506-monitor-daily.service" "${SYSTEMD_DIR}/"
cp "${SCRIPT_DIR}/c2506-monitor.timer" "${SYSTEMD_DIR}/"
cp "${SCRIPT_DIR}/c2506-monitor-daily.timer" "${SYSTEMD_DIR}/"

echo "✓ Service files copied to ${SYSTEMD_DIR}"

# Reload systemd daemon
systemctl daemon-reload
echo "✓ Systemd daemon reloaded"

# Enable timers
systemctl enable c2506-monitor.timer
systemctl enable c2506-monitor-daily.timer
echo "✓ Timers enabled"

# Start timers
systemctl start c2506-monitor.timer
systemctl start c2506-monitor-daily.timer
echo "✓ Timers started"

# Show status
echo ""
echo "Timer status:"
systemctl list-timers | grep c2506 || echo "No c2506 timers found"

echo ""
echo "Installation complete!"
echo ""
echo "Useful commands:"
echo "  systemctl status c2506-monitor.timer"
echo "  systemctl status c2506-monitor-daily.timer"
echo "  systemctl list-timers | grep c2506"
echo "  journalctl -u c2506-monitor.service"
echo ""
