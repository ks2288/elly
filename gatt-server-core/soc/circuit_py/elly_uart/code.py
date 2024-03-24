# To leverage this module, procure an Adafruit BluefruitLE-compatible SoC 
# (i.e. Bluefruit Feather Express or BBC micro:bit), and flash it with the 
# latest CircuitPython firmware. Then copy the entire contents (libs included)
# of the elly_uart directory onto its mounted CIRCUITPY drive via UFW.
# To communicate with the device via serial REPL, use a tool like minicom,
# and access the device with its mountpoint (i.e. /dev/ttyACM0 or 
# /dev/tty.usbmodem...). CircuitPython stdout will be routed to your terminal.

import time
import board
import neopixel
import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_ble.services.standard import BatteryService
from adafruit_ble.services.nordic import UARTService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement

def handle_rx(service):
    s = service.readline()
    if s:
        try:
            result = str(eval(s))
        except Exception as e:
            result = repr(e)
        service.write(result.encode("utf-8"))

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

while True :
    uart_service = UARTService()
    radio = adafruit_ble.BLERadio()
    a = ProvideServicesAdvertisement(uart_service)
    a.connectable = True
    radio.name = "MD52840"
    radio.start_advertising(a)
    print("advertising")
    info_service = DeviceInfoService(manufacturer="Adafruit", model_number="BFE52840")
    battery_service = BatteryService()
    

    while not radio.connected:
        led[0] = (0, 127, 0)
        time.sleep(0.05)
        led[0] = (0, 0, 0)
        time.sleep(2)

    while radio.connected:
        for connection in radio.connections:
            while not connection.paired:
                led[0] = (0, 127, 0)
                handle_rx(uart_service)
                
            print("paired")
            try:
                dis = connection[DeviceInfoService]
                print(dis.manufacturer)
                print(dis.model_number)
            except:
                print("Central has no Device Info Service exposed")
            while connection.paired:
                led[0] = (0, 0, 127)
                handle_rx(uart_service)
            
    print("disconnected")