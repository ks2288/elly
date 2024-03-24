# README #

### NOTE: this repo is a WIP while it gets some functional/documentation additions ###

Elly (from the "L" and "E" portions of BLE, as a truncated name) is a toolset for working with (or creating) GATT service (both client and server) implementations.

This repo contains a set of more finely-tuned Python implementations based on the examples provided by the [BLE SIG](https://www.bluetooth.com/bluetooth-resources/bluetooth-for-linux/). Primarily, this repo contains wrappers in both Python and BaSH that allow a more-streamlined process to get up-and-running quickly for development with BLE GATT services. This repo also contains a Debian (or any other variant that supports/uses Aptitude and can pull/run components from the Debian sources) setup script that will download all of the requisite dependencies using both `apt` and `pip` via Python (`pyenv` is also included).

### Code Purpose ###

This repo has two main purposes: to first provide a basic wrapper of the BLE SIG's example code that more-quickly allows testing/development of BLE GATT services via the DBUS/BlueZ APIs with Python on systems that support both BlueZ and DBUS - namely Linux-based desktops, laptops, and SoC units like the Raspberry Pi and similar IoT-friendly derivatives. The second is to offer a template for using such tools modularly within a mutliprocessing framework.

### Prerequisites ###

This list is pretty short, and consists of only two core pieces of computing hardware that each have a few caveats.

1. A Linux-equipped machine with the following specifications:
    - Kernel version 5.15LTS or above (this is simply the furthest back I went with a certain Linux device; it could go further)
    - Anything with specs as powerful as an RPi3, or better (again, this is only the least-powerful device I've used; it's pretty speedy on any modern-ish laptop/desktop)
    - a Bluetooth chipset that can be accessed by your Linux user at the device level (standalone works best, as in not a combo chip that's running all the RF comms, including both WiFi and BLE)
1. A BLE peripheral (literally any device that advertises a GATT-based service, and can be at least connected to, if not paired), with some examples being:
    * a "smart" device that offers Bluetooth control in some manner (alarm clocks, solar charge control systems, headpones, etc)
    * any BLE-equipped SoC/SoM that you have programmed to advertise a GATT service (nRF52/nRF528xx devices, Gecko boards, BGM2x/BGM2xx dev kits, etc)
    * another BLE-equipped computer that supports GATT peripheral advertisement

### Usage ###

WIP

* Scan: `python3 ~/elly/gatt-client/connection_utils.py scan` OR simply `ellyscan` from the Pi user's home directory
* Connect: `python3 ~/elly/shell/connect_discover.py [device address]`
* Reset BLE known devices: `sh ~/elly/shell/clear-ble-devices.sh` OR simply `bleclear` from the Pi user's home directory
* Reset BLE hardware: `sudo systemctl restart bluetooth`

### Output ###

The connection-based commands (scan and connect, and any others) have the ability to dispatch BLE process results through whichever means you deem most appropriate. For example, you may choose to, instead of printing results via STDOUT, use a websocket connection to send results to separate module within a multitiered system. For Elly, the command results simply end up printed as standard command feedback via the active shell used for their execution. Results that are known to be multiline/multi-element can easily be "pretty-printed" by piping the results through the Python module `json.tool`. An example can be seen within the cpnnvenience aliases generated during the setup script, specifically within the `zsh` profile creation/addendum section of the script located at `elly/shell/setup/shell-setup.sh`.

These results are meant to be generic as to increase their ability to be used in a multiprocess-oriented environment (Java's `ProcessBuilder`, for example). As such, the results carry a simple JSON string format with five KVPs/elements that are mapped to properties exposed by the BlueZ Linux framework via Python/DBUS.

The following is an example of the output received from a successful BLE scan. These sample results include five devices, with each device represented by an individual element within a JSON array.
```
[
    {
        "bdaddr": "50:5D:84:EE:3F:27",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -83
    },
    {
        "bdaddr": "55:5B:88:12:A5:3B",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -82
    },
    {
        "bdaddr": "F5:6E:A2:FD:28:42",
        "name": "SYLVANIA A19 C1-1047",
        "paired": false,
        "connected": false,
        "RSSI": -65
    },
    {
        "bdaddr": "0B:2C:D0:08:4C:34",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -60
    },
    {
        "bdaddr": "28:11:A5:90:E0:88",
        "name": "LE-Bose Color II SoundLink",
        "paired": false,
        "connected": false,
        "RSSI": -83
    },
    {
        "bdaddr": "68:64:4B:16:67:15",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -89
    }
]
```

The following represents sample results from a successful connect command, during the process of which a service discovery will take place. Upon success, the connect command will return a JSON array whose elements represent the results of the GATT service discovery process. Each element represents one of the three types of GATT attributes: services, characteristics, and descriptors

```
[
    {
        "type": "SVC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service0001",
        "uuid": "00001801-0000-1000-8000-00805f9b34fb",
        "name": "Generic Attribute Service",
        "flags": []
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service0001/char0002",
        "uuid": "00002a05-0000-1000-8000-00805f9b34fb",
        "name": "Service Changed",
        "flags": [
            "indicate"
        ]
    },
    {
        "type": "DSC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service0001/char0002/desc0004",
        "uuid": "00002902-0000-1000-8000-00805f9b34fb",
        "name": "Client Characteristic Configuration",
        "flags": []
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service0001/char0005",
        "uuid": "00002b2a-0000-1000-8000-00805f9b34fb",
        "name": "Unknown",
        "flags": [
            "read"
        ]
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service0001/char0007",
        "uuid": "00002b29-0000-1000-8000-00805f9b34fb",
        "name": "Unknown",
        "flags": [
            "read",
            "write"
        ]
    },
    {
        "type": "SVC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service000e",
        "uuid": "0000180a-0000-1000-8000-00805f9b34fb",
        "name": "Device Information Service",
        "flags": []
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service000e/char000f",
        "uuid": "00002a29-0000-1000-8000-00805f9b34fb",
        "name": "Unknown",
        "flags": [
            "read"
        ]
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service000e/char0011",
        "uuid": "00002a23-0000-1000-8000-00805f9b34fb",
        "name": "Unknown",
        "flags": [
            "read"
        ]
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service000e/char0013",
        "uuid": "00002a26-0000-1000-8000-00805f9b34fb",
        "name": "Firmware Revision String",
        "flags": [
            "read"
        ]
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service000e/char0015",
        "uuid": "00002a28-0000-1000-8000-00805f9b34fb",
        "name": "Unknown",
        "flags": [
            "read"
        ]
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service000e/char0017",
        "uuid": "00002a25-0000-1000-8000-00805f9b34fb",
        "name": "Serial Number String",
        "flags": [
            "read"
        ]
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service000e/char0019",
        "uuid": "00002a27-0000-1000-8000-00805f9b34fb",
        "name": "Unknown",
        "flags": [
            "read"
        ]
    },
    {
        "type": "SVC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b",
        "uuid": "10540b3a-fe43-4852-9808-a716860555a4",
        "name": "Unknown",
        "flags": []
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b/char001c",
        "uuid": "9a13b9e0-885e-4d6f-8f9d-d7bb288031ef",
        "name": "Unknown",
        "flags": [
            "read",
            "write-without-response",
            "write",
            "notify"
        ]
    },
    {
        "type": "DSC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b/char001c/desc001e",
        "uuid": "00002902-0000-1000-8000-00805f9b34fb",
        "name": "Client Characteristic Configuration",
        "flags": []
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b/char001f",
        "uuid": "079d266c-4196-430c-a587-c05513964ff1",
        "name": "Unknown",
        "flags": [
            "read",
            "write-without-response",
            "write",
            "notify"
        ]
    },
    {
        "type": "DSC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b/char001f/desc0021",
        "uuid": "00002902-0000-1000-8000-00805f9b34fb",
        "name": "Client Characteristic Configuration",
        "flags": []
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b/char0022",
        "uuid": "a0755bb7-3b5f-48a9-a19e-1a33b5e5a7fb",
        "name": "Unknown",
        "flags": [
            "read",
            "write-without-response",
            "write",
            "notify"
        ]
    },
    {
        "type": "DSC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b/char0022/desc0024",
        "uuid": "00002902-0000-1000-8000-00805f9b34fb",
        "name": "Client Characteristic Configuration",
        "flags": []
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b/char0025",
        "uuid": "00002a52-0000-1000-8000-00805f9b34fb",
        "name": "Unknown",
        "flags": [
            "read",
            "write-without-response",
            "write",
            "notify"
        ]
    },
    {
        "type": "DSC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service001b/char0025/desc0027",
        "uuid": "00002902-0000-1000-8000-00805f9b34fb",
        "name": "Client Characteristic Configuration",
        "flags": []
    },
    {
        "type": "SVC",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service0028",
        "uuid": "1d14d6ee-fd63-4fa1-bfa4-8f47b42119f0",
        "name": "Unknown",
        "flags": []
    },
    {
        "type": "CHR",
        "path": "/org/bluez/hci0/dev_84_BA_20_72_7E_99/service0028/char0029",
        "uuid": "f7bf3564-fb6d-4e53-88a4-5e37e0326063",
        "name": "Unknown",
        "flags": [
            "write"
        ]
    }
]
```

The preceding result properties - for both scan and connect - are only a select set of those exposed by BlueZ. The specific properties (KVPS within the JSON content) returned via Python can be added to or removed from the result content as needed. To do so, changes need to be made to the corresponding Python code where appropriate. 

In the first set of sample results involving a device scan (`elly/gatt-client/bluetooth_gap.py`, specifically the `discover_devices(timeout)` method), there are commented lines (around line 120) that serve as an example of how to add or remove properties exposed by BlueZ from your individual command results/operations. From there, they can then be moved up the Python execution tree, where in this case they are returned (printed) by the `scan(scantime="2500")` method within `connection_utils.py`, where `scantime` is the duration of the scan in milliseconds.
