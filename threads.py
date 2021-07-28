import threading
import time

class Threads(threading.Thread):
    def __init__(self, target, *args):
        self.killed = False
        print(args)
        print(target)
        l = list(args)
        l.append(lambda: self.killed)
        args = tuple(l)
        print(args)
        threading.Thread.__init__(self, None, target, *args)

    def is_alive(self):
        return not self.killed

    def kill(self):
        self.killed = True
    
    def start_thread(self):
        self.killed = False
        self.start()