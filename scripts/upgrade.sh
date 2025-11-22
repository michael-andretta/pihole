#!/bin/bash

# Script to upgrade Ubuntu OS and packages
# Usage: ./upgrade_os.sh [--dry-run] [--verbose]

set -e  # Exit on error

DRY_RUN=false
VERBOSE=false
APT_OPTS="-y"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run) DRY_RUN=true; shift ;;
        --verbose) VERBOSE=true; APT_OPTS="-y -o APT::Get::Show-Upgraded=true"; shift ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

# Suppress apt output unless verbose
if [ "$VERBOSE" = false ]; then
    APT_OPTS="$APT_OPTS -qq"
fi

SUDO=""
if [ "$DRY_RUN" = true ]; then
    SUDO="echo [DRY-RUN]"
fi

echo "=========================================="
echo "Ubuntu OS and Package Upgrade Script"
echo "=========================================="
[ "$DRY_RUN" = true ] && echo "[DRY-RUN MODE]" && echo ""

# Combined upgrade process
echo "Performing system upgrade..."
$SUDO sudo apt update $APT_OPTS && \
$SUDO sudo apt upgrade $APT_OPTS && \
$SUDO sudo apt full-upgrade $APT_OPTS && \
$SUDO sudo apt autoremove $APT_OPTS && \
$SUDO sudo apt autoclean $APT_OPTS

echo ""
echo "=========================================="
echo "Upgrade process completed successfully!"
echo "=========================================="
