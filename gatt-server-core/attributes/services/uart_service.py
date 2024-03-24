import common.server_constants as sc
import common.bluetooth_gatt as gatt
import common.bluetooth_utils as utils
import dbus
import dbus.exceptions
import dbus.service
import dbus.mainloop.glib

class UARTService(gatt.Service):
    def __init__(self, bus, path_base, index):
        print("Initializing UARTService object")
        gatt.Service.__init__(
            self, bus, path_base, index, sc.NORDIC_UART_SVC_UUID, True)
        print("Adding UARTRXCharacteristic to the service")
        # self.add_characteristic(IDPStateCharacteristic(bus, 0, self))
        # print("Adding UARTTXCharacteristic to the service")
        # self.add_characteristic(IDPStateCharacteristic(bus, 0, self))