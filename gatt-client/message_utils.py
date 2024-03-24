import json
import sys
import bluetooth_utils as utils
from pathlib import Path
home = str(Path.home()) + '/elly/gatt-client'
sys.path.insert(0, home)

def create_notification(identifier, message, path, content):
    msg = {}
    msg['notificationType'] = str(identifier)
    msg['message'] = str(message)
    msg['path'] = str(path)
    msg['content'] = content
    
    msg_json = json.JSONEncoder().encode(msg)
    return msg_json

def create_command_response(type, content, message = "Subprocess response"):
    msg = {}
    msg['type'] = type
    msg['message'] = message
    msg['content'] = content
    msg_json = json.JSONEncoder().encode(msg)
    return msg_json