#!/usr/bin/env bash
set -e

case $OSTYPE in
  darwin*)
    source setup/osx.sh
    ;;
esac
