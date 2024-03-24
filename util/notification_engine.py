import sys
import dbus
import dbus.mainloop.glib
from pathlib import Path
home = str(Path.home()) + '/.elly/core'
sys.path.insert(0, home)
import bluetooth_constants
import bluetooth_core
import bluetooth_gatt as gatt
import bluetooth_utils
import message_utils as message_utils
from gi.repository import GLib

class Notifier():
    def __init__(self, bdaddr, path, identifier):
        self.path = path
        self.bdaddr = bdaddr
        self.identifier = identifier
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SystemBus()
        self.adapter_path = bluetooth_constants.BLUEZ_NAMESPACE + bluetooth_constants.ADAPTER_NAME
        self.device_path = bluetooth_utils.device_address_to_path(bdaddr, self.adapter_path)
        self.device_proxy = self.bus.get_object(bluetooth_constants.BLUEZ_SERVICE_NAME, self.device_path)
        self.device_interface = dbus.Interface(self.device_proxy, bluetooth_constants.DEVICE_INTERFACE)

    def send_notification(self, path, content):
        msg = message_utils.create_notification(self.identifier, 'Value Changed', path, content)
        print(msg)

    def ble_notify(self, enable):
        if enable:
            gatt.enable_notifications(self.device_proxy, self.path, self.send_notification)
            msg = message_utils.create_notification(self.identifier, 'Notifications enabled',self.path, None)
            print(msg)
        else:
            gatt.disable_notifications(self.bdaddr, self.path)
            msg = message_utils.create_notification(self.identifier, 'Successfully disabled notifications', self.path, "N/A")
            print(msg)
            gatt.stop_handler()
            mainloop.quit()

            
f = open(str(Path.home()) + bluetooth_constants.BCD_MAC_CACHE_PATH, "r")
bdaddr = str(f.read())
adapter_path = bluetooth_constants.ADAPTER_PATH
char_path = sys.argv[1]
path = bluetooth_utils.device_address_to_path(bdaddr, adapter_path) + char_path
identifier = sys.argv[2]

notifier = Notifier(bdaddr, path, identifier)
notifier.ble_notify(True)
mainloop = GLib.MainLoop()
try:
    mainloop.run()
except KeyboardInterrupt:
    mainloop.quit()