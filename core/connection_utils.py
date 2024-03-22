import bluetooth_constants
import bluetooth_utils
import cgi
import dbus
import json
import os
import resource
import sys
import time
import bluetooth_gap as gap
import bluetooth_constants
import subprocess
import firewall as ble_firewall
import message_utils as msg_utils
from pathlib import Path
home = str(Path.home())

resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))    

sys.settrace
bdaddr = None
device_interface = None
device_proxy = None
props_interface = None
bus = dbus.SystemBus()

def scan():
    scantime = "2500"
    devices_discovered = gap.discover_devices(int(scantime))
    devices_allowed = ble_firewall.filter_devices(devices_discovered)
    msg = msg_utils.create_command_response('SCAN_RESULTS', devices_allowed)
    print(msg)

def is_connected():
    global bus
    global device_proxy
    global props_interface
    msg = None
    try:
        props_interface = dbus.Interface(device_proxy, bluetooth_constants.DBUS_PROPERTIES)
        connected = props_interface.Get(bluetooth_constants.DEVICE_INTERFACE,"Connected")
        if connected == 0:
            connected = False
        else:
            connected = True
        msg = msg_utils.create_command_response('IS_CONNECTED', connected)
    except:
        msg = msg_utils.create_command_response('IS_CONNECTED', False)
    print(msg)

def pair():
    global bdaddr
    msg = None
    try:
        f = open(home + bluetooth_constants.BCD_MAC_CACHE_PATH, "r")
        bdaddr = str(f.read())
        pair_status = subprocess.run(["bluetoothctl", "pair"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if pair_status.returncode == 0:
            msg = msg_utils.create_command_response("PAIR_OK", bdaddr, "Paired successfully to %s" % bdaddr)
        else:
            msg = msg_utils.create_command_response("PAIR_NOK", bdaddr, "Device %s is no longer connected" % bdaddr)
    except Exception as e:
        msg = msg_utils.create_command_response("PAIR_NOK", bdaddr, "Pairing to %s failed: " % bdaddr + str(e))
    finally:
        print(msg)

def connect():
    global bus
    global device_interface
    try:
        device_interface.Connect()
    except Exception as e:
        print("Failed to connect")
        print(e.get_dbus_name())
        print(e.get_dbus_message())
        if ("UnknownObject" in e.get_dbus_name()):
            scan()
            connect()
        return bluetooth_constants.RESULT_EXCEPTION
    else:
        print("Connection successful")
        return bluetooth_constants.RESULT_OK

def disconnect():
    global bus
    global device_interface
    global bdaddr
    try:
        f = open(home + bluetooth_constants.BCD_MAC_CACHE_PATH, "r")
        bdaddr = str(f.read())
        get_device_interface()
        device_interface.Disconnect()
    except Exception as e:
        msg = msg_utils.create_command_response("DISCONNECT_NOK", e.get_dbus_message())
        print(msg)
    else:
        msg = msg_utils.create_command_response('DISCONNECT_OK', bdaddr)
        print(msg)

def setup():
    global bdaddr
    global device_interface
    global device_proxy
    if sys.argv.count == 3:
        bdaddr = sys.argv[2]
    else:
        f = open(home + bluetooth_constants.BCD_MAC_CACHE_PATH, "r")
        bdaddr = str(f.read())
    get_device_interface()

def get_device_interface():
    global device_proxy
    global device_interface
    adapter_path = bluetooth_constants.BLUEZ_NAMESPACE + bluetooth_constants.ADAPTER_NAME
    device_path = bluetooth_utils.device_address_to_path(bdaddr, adapter_path)
    device_proxy = bus.get_object(bluetooth_constants.BLUEZ_SERVICE_NAME,device_path)
    device_interface =  dbus.Interface(device_proxy, bluetooth_constants.DEVICE_INTERFACE)

command = sys.argv[1]
if command == "scan":
    scan()
elif command == "disconnect":
    disconnect()
elif command == "pair":
    pair()
else:
    setup()
    if command == "is_connected":
        is_connected()
    elif command == "connect":
        connect()
    else:
        print("Command not recognized: " + sys.argv[1])
        print("usage: python3 ~/[path_to_file]/connection_utils.py [command] [bdaddr]")
        sys.exit(1)
