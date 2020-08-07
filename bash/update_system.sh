#!/usr/bin/env bash

# Variables #

RED='\033[0;31m' # red color
YELLOW='\033[0;33m'
NC='\033[0m' #no Color
MSG_UPDATE="Updating package information from all configured sources..."
MSG_UPGRADE="\nInstalling available upgrades of all packages currently installed
on the system from the sources configured via sources.list..."
MSG_AUTOREMOVE="\nRemoving packages that were automatically installed to satisfy
dependencies for other packages and are now no longer needed..."
MSG_CLEAN="\nClearing out the local repository of retrieved package files..."

# Functions #

function print_msg() {
    printf "${YELLOW}${*}${NC}\n"
}

# Main Script #

print_msg $MSG_UPDATE
sudo apt update

print_msg $MSG_UPGRADE
sudo apt -y upgrade

print_msg $MSG_AUTOREMOVE
sudo apt -y autoremove

print_msg $MSG_CLEAN
sudo apt -y clean

print_msg "\nExit\n"