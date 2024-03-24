#!/usr/bin/python3
import sys
from pathlib import Path
home = str(Path.home()) + '/elly/core/gatt-server-core'
sys.path.insert(0, home)
import common.advertisement as adv
import common.application as appl
from attributes.services import battery_service as bsvc
from attributes.services import idp_service as idps
from common import server_constants
from common import bluetooth_gatt
from common import bluetooth_utils
from common import bluetooth_exceptions
import dbus
import dbus.exceptions
import dbus.service
import dbus.mainloop.glib

import random
from gi.repository import GObject
from gi.repository import GLib


base_path = '/org/bluez/elly'
bus = None
adapter_path = None
adv_mgr_interface = None
connected = 0
services = []

def create_services():
    batt_svc = bsvc.BatteryService(bus, base_path, 0)
    services.append(batt_svc)
    idp_svc = idps.IDPService(bus, base_path, 1)
    services.append(idp_svc)


def register_ad_cb():
    print('Advertisement registered OK')


def register_ad_error_cb(error):
    print('Error: Failed to register advertisement: ' + str(error))
    mainloop.quit()


def register_app_cb():
    print('GATT application registered')


def register_app_error_cb(error):
    print('Failed to register application: ' + str(error))
    mainloop.quit()


def set_connected_status(status):
    if (status == 1):
        print("Central connected")
        connected = 1
        stop_advertising()
    else:
        print("Central disconnected")
        connected = 0
        start_advertising()


def properties_changed(interface, changed, invalidated, path):
    if (interface == server_constants.DEVICE_INTERFACE):
        if ("Connected" in changed):
            set_connected_status(changed["Connected"])


def interfaces_added(path, interfaces):
    if server_constants.DEVICE_INTERFACE in interfaces:
        properties = interfaces[server_constants.DEVICE_INTERFACE]
        if ("Connected" in properties):
            set_connected_status(properties["Connected"])


def stop_advertising():
    global adv
    global adv_mgr_interface
    print("Unregistering EllyAdvertisement", adv.get_path())
    adv_mgr_interface.UnregisterAdvertisement(adv.get_path())


def start_advertising():
    global adv
    global adv_mgr_interface
    print("Registering EllyAdvertisement", adv.get_path())
    adv_mgr_interface.RegisterAdvertisement(adv.get_path(), {},
                                            reply_handler=register_ad_cb,
                                            error_handler=register_ad_error_cb)


dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

adapter_path = server_constants.BLUEZ_NAMESPACE + \
    server_constants.ADAPTER_NAME
adv_mgr_interface = dbus.Interface(bus.get_object(
    server_constants.BLUEZ_SERVICE_NAME, adapter_path), server_constants.ADVERTISING_MANAGER_INTERFACE)

service_manager = dbus.Interface(
    bus.get_object(server_constants.BLUEZ_SERVICE_NAME, adapter_path),
    server_constants.GATT_MANAGER_INTERFACE)

bus.add_signal_receiver(properties_changed,
                        dbus_interface=server_constants.DBUS_PROPERTIES,
                        signal_name="PropertiesChanged",
                        path_keyword="path")

bus.add_signal_receiver(interfaces_added,
                        dbus_interface=server_constants.DBUS_OM_IFACE,
                        signal_name="InterfacesAdded")


adv_mgr_interface = dbus.Interface(bus.get_object(
    server_constants.BLUEZ_SERVICE_NAME, adapter_path), server_constants.ADVERTISING_MANAGER_INTERFACE)
adv = adv.EllyAdvertisement(bus, 0, 'peripheral', 'ellyIDP')
start_advertising()

create_services()

app = appl.MDGattApp(bus, services)

mainloop = GLib.MainLoop()

print('Registering MDGattApp...')

service_manager.RegisterApplication(app.get_path(), {},
                                    reply_handler=register_app_cb,
                                    error_handler=register_app_error_cb)

mainloop.run()
