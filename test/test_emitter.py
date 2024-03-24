import sys
import time
import json
from wsclient import ws_client

class Emitter():
    def __init__(self):
       self.client = ws_client.WsClient()

    def run(self):
        while(True):
            print("Running")
            time.sleep(5)
            count = 0
            while(count <= 4):
                time.sleep(1)
                count += 1
                message = self.create_message([str(count)])
                self.client.send_message(message)
                print("Sent: " + str(count))

    def create_message(self, content):
        msg = {}
        msg["type"] = "NOTIFICATION"
        msg["content"] = content
        msgJson = json.dumps(msg)
        return msgJson

if __name__ == "__main__":
    emitter = Emitter()
    emitter.run()