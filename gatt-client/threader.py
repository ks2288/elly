from __future__ import print_function
import sys
import message_utils
import threading
import _thread as thread

def timeout(fn_name):
    msg = message_utils.create_command_response('PROCESS_ERROR', str(fn_name) + ' timed out')
    print(msg)
    sys.stderr.flush() 
    thread.interrupt_main()

def exit_after(s, callback = timeout):
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, callback, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            except:
                msg = message_utils.create_command_response('PROCESS_ERROR', 'An error occurred calling ' + str(fn.__name__))
                print(msg)
            finally:
                timer.cancel()
            return result
        return inner
    return outer