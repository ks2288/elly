import enum
import os
import resource
import sys
import json
from pathlib import Path
home = str(Path.home()) + '/elly/core/util'
sys.path.insert(0, home)
import bluetooth_gatt as gatt
import bluetooth_core
import bluetooth_constants as constants
import bluetooth_utils as utils
import message_utils

resource.setrlimit(resource.RLIMIT_STACK,
                   (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

f = open(str(Path.home()) + constants.BCD_MAC_CACHE_PATH, "r")
bdaddr = str(f.read())

adapter_path = constants.ADAPTER_PATH
device_path = utils.device_address_to_path(bdaddr, adapter_path)

sys_id_uuid = constants.SYS_ID_CHR_UUID
sys_id_object_path = constants.SYS_ID_OBJ_PATH
sys_id_path = device_path + sys_id_object_path

manufac_name_uuid = constants.MANUFACTURER_CHR_UUID
manufac_name_obj_path = constants.MANUFACTURER_CHR_OBJ_PATH
manufac_name_path = device_path + manufac_name_obj_path

model_no_uuid = constants.MODEL_NUMBER_CHR_UUID
model_no_object_path = constants.MODEL_NUMBER_OBJ_PATH
model_no_path = device_path + model_no_object_path

serial_no_uuid = constants.SERIAL_NUMBER_CHR_UUID
serial_no_object_path = constants.SERIAL_NUMBER_OBJ_PATH
serial_no_path = device_path + serial_no_object_path

hw_rev_uuid = constants.HW_REV_CHR_UUID
hw_rev_object_path = constants.HW_REV_OBJ_PATH
hw_rev_path = device_path + hw_rev_object_path

fw_rev_uuid = constants.FW_REV_CHR_UUID
fw_rev_object_path = constants.FW_REV_OBJ_PATH
fw_rev_path = device_path + fw_rev_object_path

# TODO: add battery level when it's exposed by the device

read_path = None

def read_info_char(name):
    if name == "sys-id":
        read_value()
        return        
    elif name == "mfg-name":
        read_path = manufac_name_path
    elif name == "model-no":
        read_path = model_no_path
    elif name == "serial-no":
        read_path = serial_no_path
    elif name == "hw-rev":
        read_path = hw_rev_path
    elif name == "fw-rev":
        read_path = fw_rev_path
    msg = None
    try:
        value = gatt.read_decode_char(bdaddr, read_path)
        msg = message_utils.create_command_response('READ_OK', value, read_path)
    except Exception as e:
        msg = message_utils.create_command_response('READ_FAIL', str(e), read_path)
    finally:
        print(msg)

def read_value():
    read_path = sys_id_path
    msg = None
    try:
        value = gatt.read_raw_char(bdaddr, read_path)
        msg = message_utils.create_command_response('READ_OK', value, read_path)
    except Exception as e:
        msg = message_utils.create_command_response('READ_FAIL', str(e), read_path)
    finally:
        print(msg)

if __name__ == "__main__":
    type = sys.argv[1]
    read_info_char(type)