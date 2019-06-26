#!/usr/bin/env bash

# Change dir
pushd $(dirname "$(readlink -f "$0")") > /dev/null

echo -e "Executing in $PWD\n"

# Install Python dependencies
python -m pip install -r requirements.txt

popd > /dev/null

echo -e "\nDone!"
