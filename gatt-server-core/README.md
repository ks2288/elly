# README #

* This particular directory of Python code allows developers/engineers to quickly deploy GATT servers that have the ability to mock - quite literally - any BLE peripheral's attribute table/data structure/UUIDs/etc.

### Code Purpose ###

This code exists as a working template that provides a base of code for concrete implementations of the following BLE peripheral functionalities:

* GAP advertisements
* Attribute tables (services, characteristics, and descriptors)
* Real-time device usage simulation such as:
    * battery discharge
    * pump flow
    * implantable stimulator operation
* Sending any necessary BLE notifications

### Structure ###

The directory `elly/core/gatt-server-core` is broken down into three subdirectories: 

1. `common`
    * Contains concrete code that will run on all such implementations of Elly GATT servers
        * Advertisement class
        * Application class
        * `dbus` interface implementations
1. `services`
    * Contains service, characteristic, and descriptor class implementations
    * Houses both generalized (battery service, for example) and vendor-specific (such as the IDP service) server object implementations
        * "server object" refers to the subclass(es) and/or implementations of the `BlueZ` Python attribute classes and any necessary interfaces respectively
1. `server_apps`
    * Contains the server application code, aka the `dbus` service that will provide centrals with access to your peripheral code
    * These files contain processes wrapped within `GLib`'s `mainloop()` implementation
        * Each file represents a self-contained GATT server process

### Usage ###

When your server code has been implemented, the server can be spawned using any of the most commonly-used methods:

* From the command line using `python`
* From within a Python shell
* Creating a desktop launcher

As an example, a very simple, simulated internal diabetic pump (IDP) GATT server has been provided. To use this script, perform the following:

1. Open a new terminal window, and run the following command:
    * `python elly/core/gatt-server-core/server_apps/idp_gatt_server.py`
1. When successfully spawned, you will see the server return the following output:

```
Registering MDAdvertisement /org/bluez/elly/advertisement0
Initialising BatteryService object
Adding TemperatureCharacteristic to the service
creating Characteristic with path=/org/bluez/elly/service0/char0
Initial battery level set to 89
Initialising IDPService object
Adding IDPStateCharacteristic to the service
creating Characteristic with path=/org/bluez/elly/service1/char0
Service added at index 0
Service added at index 1
Registering MDGattApp...
GetManagedObjects
GetManagedObjects: service=/org/bluez/elly/service0
GetManagedObjects: service=/org/bluez/elly/service1
GATT application registered
{'Type': 'peripheral', 'LocalName': dbus.String('ellyIDP'), 'Discoverable': dbus.Boolean(True)}
Advertisement registered OK
```

When running, you can use a central app (like nRF Connect) to view, manipulate values within, and register for value-changed notifications of the server's attribute table.

To stop the server, simply press `ctrl + c` to kill the process from within the active terminal window. Alternatively, to perform a safe cleanup, run the following command from a separate, new terminal window with the server still running:
    * `bash ~/elly/shell/gatt-stop.sh`