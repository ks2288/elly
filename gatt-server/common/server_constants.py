#!/usr/bin/python3

ADAPTER_NAME = "hci0"

BLUEZ_SERVICE_NAME = "org.bluez"
BLUEZ_NAMESPACE = "/org/bluez/"
DBUS_PROPERTIES="org.freedesktop.DBus.Properties"
DBUS_OM_IFACE = 'org.freedesktop.DBus.ObjectManager'

ADAPTER_INTERFACE = BLUEZ_SERVICE_NAME + ".Adapter1"
DEVICE_INTERFACE = BLUEZ_SERVICE_NAME + ".Device1"
GATT_MANAGER_INTERFACE = BLUEZ_SERVICE_NAME + ".GattManager1"
GATT_SERVICE_INTERFACE = BLUEZ_SERVICE_NAME + ".GattService1"
GATT_CHARACTERISTIC_INTERFACE = BLUEZ_SERVICE_NAME + ".GattCharacteristic1"
GATT_DESCRIPTOR_INTERFACE = BLUEZ_SERVICE_NAME + ".GattDescriptor1"
ADVERTISEMENT_INTERFACE = BLUEZ_SERVICE_NAME + ".LEAdvertisement1"
ADVERTISING_MANAGER_INTERFACE = BLUEZ_SERVICE_NAME + ".LEAdvertisingManager1"

RESULT_OK = 0
RESULT_ERR = 1
RESULT_ERR_NOT_CONNECTED = 2
RESULT_ERR_NOT_SUPPORTED = 3
RESULT_ERR_SERVICES_NOT_RESOLVED = 4	
RESULT_ERR_WRONG_STATE = 5
RESULT_ERR_ACCESS_DENIED = 6
RESULT_EXCEPTION = 7
RESULT_ERR_BAD_ARGS = 8
RESULT_ERR_NOT_FOUND = 9

UUID_NAMES = {
    "00001801-0000-1000-8000-00805f9b34fb" : "Generic Attribute Service",
    "0000180a-0000-1000-8000-00805f9b34fb" : "Device Information Service",
    "e95d93b0-251d-470a-a062-fa1922dfa9a8" : "DFU Control Service",
    "e95d93af-251d-470a-a062-fa1922dfa9a8" : "Event Service",
    "e95d9882-251d-470a-a062-fa1922dfa9a8" : "Button Service",
    "e95d6100-251d-470a-a062-fa1922dfa9a8" : "Temperature Service",
    "e95dd91d-251d-470a-a062-fa1922dfa9a8" : "LED Service",
    "00002a05-0000-1000-8000-00805f9b34fb" : "Service Changed",
    "e95d93b1-251d-470a-a062-fa1922dfa9a8" : "DFU Control",
    "00002a24-0000-1000-8000-00805f9b34fb" : "Model Number String",
    "00002a25-0000-1000-8000-00805f9b34fb" : "Serial Number String",
    "00002a26-0000-1000-8000-00805f9b34fb" : "Firmware Revision String",
    "e95d5404-251d-470a-a062-fa1922dfa9a8" : "Client Event",
    "e95d23c4-251d-470a-a062-fa1922dfa9a8" : "Client Requirements",
    "00002902-0000-1000-8000-00805f9b34fb" : "Client Characteristic Configuration",
}    

DEVICE_INF_SVC_UUID = "0000180a-0000-1000-8000-00805f9b34fb"
MODEL_NUMBER_UUID    = "00002a24-0000-1000-8000-00805f9b34fb"

BATTERY_SVC_UUID = "0000180f-0000-1000-8000-00805f9b34fb"
BATTERY_LVL_CHAR_UUID = "00002a19-0000-1000-8000-00805f9b34fb"
BATTERY_PWR_STATE_CHAR_UUID = "00002a1a-0000-1000-8000-00805f9b34fb"
BATTERY_LVL_STATE_CHAR_UUID = "00002a1b-0000-1000-8000-00805f9b34fb"

TEMPERATURE_SVC_UUID = "e95d6100-251d-470a-a062-fa1922dfa9a8"
TEMPERATURE_CHR_UUID = "e95d9250-251d-470a-a062-fa1922dfa9a8"

IDP_SVC_UUID = "6e400009-b5a3-f393-e0a9-e50e24dcca9e"
IDP_STATE_CHR_UUID = "6e400008-b5a3-f393-e0a9-e50e24dcca9e"

NORDIC_UART_SVC_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
NORDIC_UART_RX_CHR_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
NORDIC_UART_TX_CHR_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
