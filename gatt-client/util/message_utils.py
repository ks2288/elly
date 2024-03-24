import json
import sys


def create_notification(identifier, message, path, content):
    msg = {}
    msg['notificationType'] = str(identifier)
    msg['message'] = str(message)
    msg['path'] = str(path)
    msg['content'] = content
    msg_json = json.JSONEncoder().encode(msg)
    return msg_json

def create_command_response(type, message):
    msg = {}
    msg['type'] = type
    msg['content'] = message
    msg_json = json.JSONEncoder().encode(msg)
    return msg_json