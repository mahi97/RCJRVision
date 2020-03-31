#!/bin/bash
set -e
set -x

PYTHON_COMMAND=python
PIP_COMMAND=pip
if [ "$TRAVIS_OS_NAME" == "osx" ]
then
    PYTHON_COMMAND=python3
    PIP_COMMAND=pip3
fi

$PIP_COMMAND install -r requirements.txt

if [ "$TRAVIS_OS_NAME" == "osx" ]
then
  $PIP_COMMAND install --upgrade --upgrade-strategy=only-if-needed -r dev-requirements.txt --user
else
  $PIP_COMMAND install --upgrade --upgrade-strategy=only-if-needed -r dev-requirements.txt
fi
