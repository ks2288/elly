import common.server_constants as sc
# import bluetooth_gatt
# import bluetooth_utils
import common.bluetooth_exceptions as btexc
import dbus
import dbus.exceptions
import dbus.service
import dbus.mainloop.glib

class EllyAdvertisement(dbus.service.Object):
    PATH_BASE = '/org/bluez/elly/advertisement'

    def __init__(self, bus, index, advertising_type, name):
        self.path = self.PATH_BASE + str(index)
        self.bus = bus
        self.ad_type = advertising_type
        self.service_uuids = None
        self.manufacturer_data = None
        self.solicit_uuids = None
        self.service_data = None
        self.local_name = name
        self.include_tx_power = False
        self.data = None
        self.discoverable = True
        dbus.service.Object.__init__(self, bus, self.path)

    def get_properties(self):
        properties = dict()
        properties['Type'] = self.ad_type
        if self.service_uuids is not None:
            properties['ServiceUUIDs'] = dbus.Array(self.service_uuids,
                                                    signature='s')
        if self.solicit_uuids is not None:
            properties['SolicitUUIDs'] = dbus.Array(self.solicit_uuids,
                                                    signature='s')
        if self.manufacturer_data is not None:
            properties['ManufacturerData'] = dbus.Dictionary(
                self.manufacturer_data, signature='qv')
        if self.service_data is not None:
            properties['ServiceData'] = dbus.Dictionary(self.service_data,
                                                        signature='sv')
        if self.local_name is not None:
            properties['LocalName'] = dbus.String(self.local_name)
        if self.discoverable is not None and self.discoverable == True:
            properties['Discoverable'] = dbus.Boolean(self.discoverable)
        if self.include_tx_power:
            properties['Includes'] = dbus.Array(["tx-power"], signature='s')

        if self.data is not None:
            properties['Data'] = dbus.Dictionary(
                self.data, signature='yv')
        print(properties)
        return {sc.ADVERTISING_MANAGER_INTERFACE: properties}

    def get_path(self):
        return dbus.ObjectPath(self.path)

    @dbus.service.method(sc.DBUS_PROPERTIES,
                         in_signature='s',
                         out_signature='a{sv}')
    def GetAll(self, interface):
        if interface != sc.ADVERTISEMENT_INTERFACE:
            raise btexc.InvalidArgsException()
        return self.get_properties()[sc.ADVERTISING_MANAGER_INTERFACE]

    @dbus.service.method(sc.ADVERTISING_MANAGER_INTERFACE,
                         in_signature='',
                         out_signature='')
    def Release(self):
        print('%s: Released' % self.path)
