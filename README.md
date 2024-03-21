# README #

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

* Scan: `python3 ~/elly/core/connection_utils.py scan` OR simply `blescan` from the Pi user's home directory
* Connect: `python3 ~/elly/shell/connect_discover.py [device address]`
* Reset BLE known devices: `sh ~/elly/shell/clear-ble-devices.sh` OR simply `bleclear` from the Pi user's home directory
* Reset BLE hardware: `sudo systemctl restart bluetooth`

### Output ###

The connection-based commands (scan and connect, and any others) have the ability to dispatch BLE process results through whichever means you deem most appropriate. For Mock Dev, the command server leverages CGI to read directly from STDOUT for any relevant callback-type information. 

The server also spawns, monitors, and controls each individual process through to its completion (errors included). As such, the two aforementioned example commands will simply "print" any resulting process feedback. If you run these scripts from the command line, expect to see the output in a way similar to any you've seen in the past when executing shell commands. However, any JRE ProcessBuilder treats these as callbacks from a given process, and the developer has the ability to handle them as such - in a purely reactive manner with little-to-no code overhead. For these examples, JSON strings are leveraged as a low-cost, efficient way to handle abstracted messaging from client to server to peripheral all the way back to client again in a manner that is entirely sovereign of the actual BLE functionality.

Example output from a device scan:
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
        "bdaddr": "48:9E:BD:86:10:38",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -79
    },
    {
        "bdaddr": "58:F5:3E:21:11:CB",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -47
    },
    {
        "bdaddr": "F5:6E:A2:FD:28:42",
        "name": "SYLVANIA A19 C1-1047",
        "paired": false,
        "connected": false,
        "RSSI": -65
    },
    {
        "bdaddr": "6C:D0:70:1B:01:84",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -49
    },
    {
        "bdaddr": "70:2A:5D:38:08:AF",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -51
    },
    {
        "bdaddr": "66:7E:FE:F4:DB:07",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -58
    },
    {
        "bdaddr": "6D:26:E6:02:B4:91",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -83
    },
    {
        "bdaddr": "84:BA:20:72:7E:99",
        "name": "NGT",
        "paired": false,
        "connected": false,
        "RSSI": -66
    },
    {
        "bdaddr": "08:F7:50:7C:39:77",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -60
    },
    {
        "bdaddr": "49:A8:21:EC:08:58",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -86
    },
    {
        "bdaddr": "60:B9:8B:B8:60:69",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -77
    },
    {
        "bdaddr": "52:1F:22:A6:57:B1",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -85
    },
    {
        "bdaddr": "61:59:6A:6D:66:21",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -73
    },
    {
        "bdaddr": "10:91:A2:7C:12:C2",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -85
    },
    {
        "bdaddr": "61:96:20:A0:82:33",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -59
    },
    {
        "bdaddr": "6E:8C:56:E4:6B:CE",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -76
    },
    {
        "bdaddr": "47:41:DB:D0:0D:36",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -83
    },
    {
        "bdaddr": "52:24:CD:77:07:4F",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -86
    },
    {
        "bdaddr": "04:EE:03:EC:59:80",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -92
    },
    {
        "bdaddr": "DD:C8:5E:04:26:39",
        "name": "NB1TM",
        "paired": false,
        "connected": false,
        "RSSI": -79
    },
    {
        "bdaddr": "5F:DE:DC:2A:42:16",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -60
    },
    {
        "bdaddr": "74:AE:34:31:5B:D2",
        "name": "Unknown",
        "paired": false,
        "connected": false,
        "RSSI": -56
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

Example output from connection (includes service discovery, and will return discoveries upon success):

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

These dictionaries are completely arbitrary per implementation, and may be tweaked on an as-needed basis per project from within both the Python and JVM server code (a KMP data model library is in progress to eliminate the need to edit the code in multiple places).
