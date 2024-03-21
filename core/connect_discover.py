#!/usr/bin/python3
#
# Connects to a specified device
# Run from the command line with a bluetooth device address argument

import bluetooth_constants
import bluetooth_utils
import bluetooth_gap as gap
import dbus
import dbus.mainloop.glib
import message_utils
import os
import resource
import sys
import time
from gi.repository import GLib
from pathlib import Path
import threader
import _thread as thread
home = str(Path.home())
sys.path.insert(0, home)

resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

bus = None
device_interface = None
device_path = None
found_dis = False
found_mn  = False
dis_path = None
mn_path  = None
attributes = []

def service_discovery_completed():
    global found_dis
    global found_mn
    global dis_path
    global mn_path
    global bus
    
    bus.remove_signal_receiver(interfaces_added,"InterfacesAdded")
    bus.remove_signal_receiver(properties_changed,"PropertiesChanged")
    mainloop.quit()
    
def properties_changed(interface, changed, invalidated, path):
    global device_path
    if path != device_path:
        return

    if 'ServicesResolved' in changed:
        sr = bluetooth_utils.dbus_to_python(changed['ServicesResolved'])
        if sr == True:
            service_discovery_completed()
        
def interrupt(fn_name):
    msg = message_utils.create_command_response('PROCESS_ERROR', str(fn_name) + ' timed out')
    print(msg)
    mainloop.quit()

def interfaces_added(path, interfaces):
    global found_dis
    global found_mn
    global dis_path
    global mn_path
    global attributes
    if bluetooth_constants.GATT_SERVICE_INTERFACE in interfaces:
        properties = interfaces[bluetooth_constants.GATT_SERVICE_INTERFACE]
        service = {}
        service["type"] = "SVC"
        service["path"] = path
        if 'UUID' in properties:
            uuid = properties['UUID']
            if uuid == bluetooth_constants.DEVICE_INF_SVC_UUID:
                found_dis = True
                dis_path = path
            service["uuid"] = bluetooth_utils.dbus_to_python(uuid)
            service["name"] = bluetooth_utils.get_name_from_uuid(uuid)
            attributes.append(service)
        service["flags"] = []
        return

    if bluetooth_constants.GATT_CHARACTERISTIC_INTERFACE in interfaces:
        characteristic = {}
        characteristic["type"] = "CHR"
        characteristic["path"] = path
        properties = interfaces[bluetooth_constants.GATT_CHARACTERISTIC_INTERFACE]
        if 'UUID' in properties:
            uuid = properties['UUID']
            if uuid == bluetooth_constants.MODEL_NUMBER_CHR_UUID:
                found_mn = True
                mn_path = path
            characteristic["uuid"] = bluetooth_utils.dbus_to_python(uuid)
            characteristic["name"] = bluetooth_utils.get_name_from_uuid(uuid)
            flags  = []
            for flag in properties['Flags']:
                flags.append(flag)
            characteristic["flags"] = flags
            attributes.append(characteristic)
        return
    
    if bluetooth_constants.GATT_DESCRIPTOR_INTERFACE in interfaces:
        properties = interfaces[bluetooth_constants.GATT_DESCRIPTOR_INTERFACE]
        descriptor = {}
        descriptor["type"] = "DSC"
        descriptor["path"] = path
        
        if 'UUID' in properties:
            uuid = properties['UUID']
            descriptor["uuid"] = bluetooth_utils.dbus_to_python(uuid)
            descriptor["name"] = bluetooth_utils.get_name_from_uuid(uuid)
            attributes.append(descriptor)
        descriptor["flags"] = []
        return


def connect():
    global bus
    global device_interface
    try:
        device_interface.Connect()
    except Exception as e:
        return bluetooth_constants.RESULT_EXCEPTION
    else:
        f = open(home + bluetooth_constants.BCD_MAC_CACHE_PATH, "w")
        f.write(bdaddr)
        f.close()
        return bluetooth_constants.RESULT_OK


if (len(sys.argv) != 2):
    print("usage: python3 discover_services.py [bdaddr]")
    sys.exit(1)

bdaddr = sys.argv[1]
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()
adapter_path = bluetooth_constants.BLUEZ_NAMESPACE + bluetooth_constants.ADAPTER_NAME
device_path = bluetooth_utils.device_address_to_path(bdaddr, adapter_path)
device_proxy = bus.get_object(bluetooth_constants.BLUEZ_SERVICE_NAME,device_path)
device_interface = dbus.Interface(device_proxy, bluetooth_constants.DEVICE_INTERFACE)

GLib.timeout_add(4000, connect)

bus.add_signal_receiver(interfaces_added,
        dbus_interface = bluetooth_constants.DBUS_OM_IFACE,
        signal_name = "InterfacesAdded")
bus.add_signal_receiver(properties_changed,
        dbus_interface = bluetooth_constants.DBUS_PROPERTIES,
        signal_name = "PropertiesChanged",
        path_keyword = "path")
mainloop = GLib.MainLoop()
try:
    mainloop.run()
except KeyboardInterrupt:
    mainloop.quit()
    sys.exit(1)
msg = message_utils.create_command_response('CONNECT_OK', attributes)
print(msg)