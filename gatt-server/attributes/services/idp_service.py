import common.server_constants as sc
import common.bluetooth_gatt as gatt
import common.bluetooth_utils as utils
import dbus
import dbus.exceptions
import dbus.service
import dbus.mainloop.glib

class IDPStateCharacteristic(gatt.Characteristic):

    enabled = False
    notifying = False
    
    def __init__(self, bus, index, service):
        gatt.Characteristic.__init__(
                self, bus, index,
                sc.IDP_STATE_CHR_UUID,
                ['read','write','notify'],
                service)

    def WriteValue(self, value, options):
        bool_value = utils.dbus_to_python(dbus.Boolean(value))
        self.enabled = bool_value
        print(str(self.enabled) + ' written to enabled ')

    def ReadValue(self, options):
        print('ReadValue in IDPStateCharacteristic called')
        print('Enabled: ' + str(self.enabled))
        value = []
        value.append(dbus.Boolean(self.enabled))
        return value

    def notify_idp_state(self):
        value = []
        value.append(dbus.Boolean(self.enabled))
        if self.notifying:
            print("Notification: enabled = "+str(self.enabled))
        self.PropertiesChanged(sc.GATT_CHARACTERISTIC_INTERFACE, { 'Value': value }, [])
        return self.notifying

    def StartNotify(self):
        print("Starting IDP state notifications")
        self.notifying = True

    def StopNotify(self):
        print("Stopping IDP state notifications")
        self.notifying = False


class IDPService(gatt.Service):

    def __init__(self, bus, path_base, index):
        print("Initialising IDPService object")
        gatt.Service.__init__(
            self, bus, path_base, index, sc.IDP_SVC_UUID, True)
        print("Adding IDPStateCharacteristic to the service")
        self.add_characteristic(IDPStateCharacteristic(bus, 0, self))