import common.server_constants as sc
import common.bluetooth_gatt as gatt
import dbus
import dbus.exceptions
import dbus.service
import dbus.mainloop.glib
from gi.repository import GObject
from gi.repository import GLib
import random

class BatteryService(gatt.Service):

     def __init__(self, bus, path_base, index):
        print("Initialising BatteryService object")
        gatt.Service.__init__(self, bus, path_base, index, sc.BATTERY_SVC_UUID, True)
        print("Adding TemperatureCharacteristic to the service")
        self.add_characteristic(BatteryLevelCharacteristic(bus, 0, self))

class BatteryLevelCharacteristic(gatt.Characteristic):
    batt_level_value = 0
    discharge_multiple = 1
    discharge_interval =  360000
    notifying = False
    
    def __init__(self, bus, index, service):
        global timer_id
        gatt.Characteristic.__init__(
                self, bus, index,
                sc.BATTERY_LVL_CHAR_UUID,
                ['read','notify'],
                service)
        self.batt_level_value = random.randint(85, 100)
        print("Initial battery level set to "+str(self.batt_level_value))
        timer_id = GLib.timeout_add(self.discharge_interval, self.simulate_discharge)

    def simulate_discharge(self):
        self.batt_level_value = self.batt_level_value - self.discharge_multiple
     
        print("Simulated bettery level: "+str(self.batt_level_value)+"%")
        if self.notifying:
            self.notify_battery_level()

        GLib.timeout_add(self.discharge_interval, self.simulate_discharge)

    def ReadValue(self, options):
        print('ReadValue in BatteryLevelCharacteristic called')
        print('Simulated battery level: ' + str(self.batt_level_value))
        value = []
        value.append(dbus.Byte(self.batt_level_value))
        return value
    
    def notify_battery_level(self):
        value = []
        value.append(dbus.Byte(self.batt_level_value))
        if self.notifying:
            print("Notification: simulated battery level = "+str(self.batt_level_value))
        self.PropertiesChanged(sc.GATT_CHARACTERISTIC_INTERFACE, { 'Value': value }, [])
        return self.notifying

    def StartNotify(self):
        print("Starting battery level notifications")
        self.notifying = True

    def StopNotify(self):
        print("Stopping battery level notifications")
        self.notifying = False
