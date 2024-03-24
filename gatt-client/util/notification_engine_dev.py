import sys
import dbus
import dbus.mainloop.glib
from pathlib import Path
home = str(Path.home()) + '/'
sys.path.insert(0, home)
import bluetooth_constants
import bluetooth_core
import bluetooth_gatt as gatt
import bluetooth_utils
import message_utils as message_utils
import json
from gi.repository import GLib
import time

class Notifier():
    def __init__(self, bdaddr, path, identifier):
        self.path = path
        self.bdaddr = bdaddr
        self.identifier = identifier
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SystemBus()
        self.adapter_path = bluetooth_constants.BLUEZ_NAMESPACE + bluetooth_constants.ADAPTER_NAME
        print("Adapter path: " + self.adapter_path)
        self.device_path = bluetooth_utils.device_address_to_path(bdaddr, self.adapter_path)
        print("Device path: " + str(self.device_path))
        self.device_proxy = self.bus.get_object(bluetooth_constants.BLUEZ_SERVICE_NAME, self.device_path)
        print("Device proxy: " + str(self.device_proxy))
        self.device_interface = dbus.Interface(self.device_proxy, bluetooth_constants.DEVICE_INTERFACE)
        print("Device interface: " + str(self.device_interface))


    def create_response(self, type, content):
        return {"type": type, "content": content}


    def send_notification(self, path, content):
        msg = message_utils.create_notification(self.identifier, "Value Changed", path, content)
        print(msg)


    def ble_notify(self, enable):
        if enable:
            gatt.enable_notifications(self.device_proxy, self.path, self.send_notification)
            msg = self.create_response("NOTIFY_ENABLED", self.path)
            msgJson = json.JSONEncoder().encode(msg)
            print(msgJson)
        else:
            gatt.disable_notifications(self.bdaddr, self.path)
            msg = message_utils.create_notification(self.identifier, "Successfully disabled notifications", self.path, "N/A")
            msgJson = json.JSONEncoder().encode(msg)
            print(msgJson)
            gatt.stop_handler()
            mainloop.quit()

    

            
bdaddr = sys.argv[1]
path = sys.argv[2]
identifier = sys.argv[3]
notifier = Notifier(bdaddr, path, identifier)
time.sleep(2)
notifier.ble_notify(True)
mainloop = GLib.MainLoop()
mainloop.run()
sys.exit(0)