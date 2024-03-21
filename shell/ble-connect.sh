#!/bin/bash

if [ $# -eq 0 ]
then 
    echo "Please provide a device address"
else
    python ~/elly/core/connect_discover.py $1
fi