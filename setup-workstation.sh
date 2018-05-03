#!/usr/bin/env bash
set -e

case $OSTYPE in
  darwin*)
    source setup/osx.sh
    ;;
  msys*)
    setup/windows.ps1
    ;;
esac
