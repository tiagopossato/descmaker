#!/usr/bin/env bash

# array with list of dependencies
declare -a dependencies=(
    "python3"
    "python3-pip"
    "python3-venv"
)

# loop through dependencies
for dependency in "${dependencies[@]}"
do
    # check if dependency is installed
    if ! dpkg -s $dependency > /dev/null 2>&1; then
        # install dependency
        sudo apt install $dependency
    fi
done


# Create virtual environment
python3 -m venv env

# Activate virtual environment
source env/bin/activate

#install app dependencies
pip install -r requirements.txt