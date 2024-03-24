#!/bin/bash

python ~/elly/gatt-client/connection_utils.py disconnect
bash ~/elly/shell/refresh-ble.sh > /dev/null 2>&1
pkill -f -9 notification