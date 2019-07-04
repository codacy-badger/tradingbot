#!/usr/bin/env bash

# Change dir
pushd $(dirname "$(readlink -f "$0")") > /dev/null

echo -e "Executing in $PWD\n"

# Install Python dependencies
python -m pip install -r requirements.txt

# Install Git hooks
python -m pip install pre-commit
pre-commit install

popd > /dev/null

echo -e "\nDone!"
