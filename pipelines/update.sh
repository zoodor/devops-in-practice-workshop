#!/bin/bash
set -xe

CWD=$(cd $(dirname $0) && pwd)
for pipeline in $CWD/*.py; do
  docker run -it --rm -v "$CWD":/usr/src/meta -w /usr/src/meta python:2.7-slim /bin/bash -c "pip install gomatic && python $(basename $pipeline)"
done
