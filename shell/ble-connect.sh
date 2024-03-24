#!/bin/bash

if [ $# -eq 0 ]
then 
    echo "Please provide a device address"
else
    python ~/elly/gatt-client/connect_discover.py $1
fi