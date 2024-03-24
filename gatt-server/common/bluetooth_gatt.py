#!/usr/bin/python3
#

import dbus
import dbus.exceptions
import dbus.service
import common.server_constants as sc
import common.bluetooth_exceptions as btexc
import sys
sys.path.insert(0, '.')

class Service(dbus.service.Object):
    """
    org.bluez.GattService1 interface implementation
    """

    def __init__(self, bus, path_base, index, uuid, primary):
        self.path = path_base + "/service" + str(index)
        self.bus = bus
        self.uuid = uuid
        self.primary = primary
        self.characteristics = []
        dbus.service.Object.__init__(self, bus, self.path)

    def get_properties(self):
        return {
                sc.GATT_SERVICE_INTERFACE: {
                        'UUID': self.uuid,
                        'Primary': self.primary,
                        'Characteristics': dbus.Array(
                                self.get_characteristic_paths(),
                                signature='o')
                }
        }

    def get_path(self):
        return dbus.ObjectPath(self.path)

    def add_characteristic(self, characteristic):
        self.characteristics.append(characteristic)

    def get_characteristic_paths(self):
        result = []
        for chrc in self.characteristics:
            result.append(chrc.get_path())
        return result

    def get_characteristics(self):
        return self.characteristics

    @dbus.service.method(sc.DBUS_PROPERTIES,
                         in_signature='s',
                         out_signature='a{sv}')
    def GetAll(self, interface):
        if interface != sc.GATT_SERVICE_INTERFACE:
            raise btexc.btexc.InvalidArgsException()

        return self.get_properties()[sc.GATT_SERVICE_INTERFACE]


class Characteristic(dbus.service.Object):
    """
    org.bluez.GattCharacteristic1 interface implementation
    """
    def __init__(self, bus, index, uuid, flags, service):
        self.path = service.path + '/char' + str(index)
        print("creating Characteristic with path="+self.path)
        self.bus = bus
        self.uuid = uuid
        self.service = service
        self.flags = flags
        self.descriptors = []
        dbus.service.Object.__init__(self, bus, self.path)

    def get_properties(self):
        return {
                sc.GATT_CHARACTERISTIC_INTERFACE: {
                        'Service': self.service.get_path(),
                        'UUID': self.uuid,
                        'Flags': self.flags,
                        'Descriptors': dbus.Array(
                                self.get_descriptor_paths(),
                                signature='o')
                }
        }

    def get_path(self):
        return dbus.ObjectPath(self.path)

    def add_descriptor(self, descriptor):
        self.descriptors.append(descriptor)

    def get_descriptor_paths(self):
        result = []
        for desc in self.descriptors:
            result.append(desc.get_path())
        return result

    def get_descriptors(self):
        return self.descriptors

    @dbus.service.method(sc.DBUS_PROPERTIES,
                         in_signature='s',
                         out_signature='a{sv}')
    def GetAll(self, interface):
        if interface != sc.GATT_CHARACTERISTIC_INTERFACE:
            raise btexc.btexc.InvalidArgsException()

        return self.get_properties()[sc.GATT_CHARACTERISTIC_INTERFACE]

    @dbus.service.method(sc.GATT_CHARACTERISTIC_INTERFACE,
                        in_signature='a{sv}',
                        out_signature='ay')
    def ReadValue(self, options):
        print('Default ReadValue called, returning error')
        raise btexc.NotSupportedException()

    @dbus.service.method(sc.GATT_CHARACTERISTIC_INTERFACE, in_signature='aya{sv}')
    def WriteValue(self, value, options):
        print('Default WriteValue called, returning error')
        raise btexc.NotSupportedException()

    @dbus.service.method(sc.GATT_CHARACTERISTIC_INTERFACE)
    def StartNotify(self):
        print('Default StartNotify called, returning error')
        raise btexc.NotSupportedException()

    @dbus.service.method(sc.GATT_CHARACTERISTIC_INTERFACE)
    def StopNotify(self):
        print('Default StopNotify called, returning error')
        raise btexc.NotSupportedException()

    @dbus.service.signal(sc.DBUS_PROPERTIES,
                         signature='sa{sv}as')
    def PropertiesChanged(self, interface, changed, invalidated):
        pass


class Descriptor(dbus.service.Object):
    """
    org.bluez.GattDescriptor1 interface implementation
    """
    def __init__(self, bus, index, uuid, flags, characteristic):
        self.path = characteristic.path + '/desc' + str(index)
        self.bus = bus
        self.uuid = uuid
        self.flags = flags
        self.chrc = characteristic
        dbus.service.Object.__init__(self, bus, self.path)

    def get_properties(self):
        return {
                sc.GATT_DESCRIPTOR_INTERFACE: {
                        'Characteristic': self.chrc.get_path(),
                        'UUID': self.uuid,
                        'Flags': self.flags,
                }
        }

    def get_path(self):
        return dbus.ObjectPath(self.path)

    @dbus.service.method(sc.DBUS_PROPERTIES,
                         in_signature='s',
                         out_signature='a{sv}')
    def GetAll(self, interface):
        if interface != sc.GATT_DESCRIPTOR_INTERFACE:
            raise btexc.InvalidArgsException()

        return self.get_properties()[sc.GATT_DESCRIPTOR_INTERFACE]

    @dbus.service.method(sc.GATT_DESCRIPTOR_INTERFACE,
                        in_signature='a{sv}',
                        out_signature='ay')
    def ReadValue(self, options):
        print ('Default ReadValue called, returning error')
        raise btexc.NotSupportedException()

    @dbus.service.method(sc.GATT_DESCRIPTOR_INTERFACE, in_signature='aya{sv}')
    def WriteValue(self, value, options):
        print('Default WriteValue called, returning error')
        raise btexc.NotSupportedException()
