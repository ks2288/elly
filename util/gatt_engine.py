from cmath import pi
from ctypes import sizeof
import os
import resource
import sys
from unittest import result
from pathlib import Path
home = str(Path.home()) + '/.elly/core'
sys.path.insert(0, home)
import bluetooth_gatt as gatt
import bluetooth_core
import bluetooth_constants as constants
import bluetooth_utils as utils
import message_utils

resource.setrlimit(resource.RLIMIT_STACK,
                   (resource.RLIM_INFINITY, 
                   resource.RLIM_INFINITY))

f = open(str(Path.home()) + constants.BCD_MAC_CACHE_PATH, "r")
bdaddr = str(f.read())
adapter_path = constants.ADAPTER_PATH

def write_to_char(bdaddr, path, buffer):
    msg = None
    try:
        written = gatt.write_characteristic(bdaddr, path, buffer)
        byte_vals = utils.dbus_to_python(written)
        msg = message_utils.create_command_response('WRITE_OK', str(byte_vals), path)        
    except Exception as e:
        msg = message_utils.create_command_response('WRITE_FAIL', str(e), path)
    finally:
        return msg

def read_from_char(bdaddr, path):
    try:
        buffer = gatt.read_characteristic(bdaddr, path)
        result = utils.dbus_to_python(buffer)
        msg = message_utils.create_command_response('READ_OK', str(result), path)
        return msg
    except Exception as e:
        msg = message_utils.create_command_response('READ_FAIL', str(e), path)
        return msg

def encode_content(content):
    encoded = None
    content_list = str(content).split(',')
    try:
        for c in content_list:
            encoded.append(int(c))
        encoded = bytearray(encoded)
    except:
        encoded = bytes(content, 'ascii')
    finally:
        return encoded

command = sys.argv[1]
char_path = sys.argv[2]
path = utils.device_address_to_path(bdaddr, adapter_path) + char_path

if command == "read":
    result = read_from_char(bdaddr, path)
    print(result)

elif command == "write":
    content = sys.argv[3]
    encoded = encode_content(content)
    byte_vals = bytearray(encoded)
    result = write_to_char(bdaddr, path, byte_vals)
    print(result)

else:
    print("Command not recognized: " + command)
    print("usage: python3 ~/.elly/core/platform/gatt_engine.py [command] [path] [optional content]")
    sys.exit(1)