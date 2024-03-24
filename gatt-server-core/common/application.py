import common.server_constants as sc
import dbus
import dbus.exceptions
import dbus.service
import dbus.mainloop.glib

class MDGattApp(dbus.service.Object):

    """
    org.bluez.GattApplication1 interface implementation
    """
    def __init__(self, bus, services):
        self.path = '/'
        self.services = []
        dbus.service.Object.__init__(self, bus, self.path)

        for index, service in enumerate(services):
            self.add_service(service)
            print("Service added at index " + str(index))

    def get_path(self):
        return dbus.ObjectPath(self.path)

    def add_service(self, service):
        self.services.append(service)

    @dbus.service.method(sc.DBUS_OM_IFACE, out_signature='a{oa{sa{sv}}}')
    def GetManagedObjects(self):
        response = {}
        print('GetManagedObjects')

        for service in self.services:
            print("GetManagedObjects: service="+service.get_path())
            response[service.get_path()] = service.get_properties()
            chrcs = service.get_characteristics()
            for chrc in chrcs:
                response[chrc.get_path()] = chrc.get_properties()
                descs = chrc.get_descriptors()
                for desc in descs:
                    response[desc.get_path()] = desc.get_properties()

        return response
