#!/bin/bash

for device in $(bluetoothctl devices | grep -o "[[:xdigit:]:]\{11,17\}"); do
    bluetoothctl remove $device > /dev/null 2>&1
done

# force kill all processes matching the platform directory pattern
pkill -f -9 elly/core/platform

# finally, restart the service
sudo systemctl restart bluetooth

echo '{type: PROCESS_OK, content: "BLE Refresh Sucessful"}'