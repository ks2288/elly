#!/usr/bin/python3
import sys
import time

class Looper():
    def __init__(self):
        self.val1 = 1
        self.val2 = 2
        self.val3 = 3

    def test1(self):
        sys.stdout.write("test 1 invoked")
        sys.stdout.write("test val 1 = " + str(self.val1))

    def test2(self):
        sys.stdout.write("test 2 invoked")
        sys.stdout.write("test val 2 = " + str(self.val2))

    def test3(self):
        sys.stdout.write("test 3 invoked")
        sys.stdout.write("test val 3 = " + str(self.val3))

    def awaitInput(self):
        try:
            msg = input()
            return msg
        except EOFError:
            self.awaitInput()

    def run(self):
        while(True):
            for msg in open(0):
                if msg.rstrip() == "1":
                    self.test1()
                elif msg.rstrip() == "2":
                    self.test2()
                elif msg.rstrip() == "3":
                    self.test3()
                elif msg.rstrip() == "SIGKILL":
                    sys.stdout.write("exiting py process...")
                    sys.exit(0)
                else:
                    sys.stdout.write("Input not recognized")

if __name__ == "__main__":
    import sys
    looper = Looper()
    looper.run()
