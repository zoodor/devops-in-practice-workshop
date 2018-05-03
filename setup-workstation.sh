#!/usr/bin/env bash
set -e

case $OSTYPE in
  darwin*)
    source setup/osx.sh
    ;;
  msys*)
    setup/windows.ps1
    ;;
  linux*)
    DISTRO=$(awk -F= '/^ID=/{print $2}' /etc/os-release | tr '"' '\0')
    case $DISTRO in
      ubuntu|debian)
        source setup/ubuntu.sh
        ;;
      centos|rhel|fedora)
        source setup/centos.sh
        ;;
    esac
    ;;
esac
