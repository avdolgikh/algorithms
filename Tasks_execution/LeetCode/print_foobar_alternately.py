
# https://docs.python.org/3/library/threading.html#event-objects

import threading

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_event = threading.Event()
        self.bar_event = threading.Event()        
        self.bar_event.clear()
        self.foo_event.set()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):                        
            self.foo_event.wait()
            printFoo()
            self.foo_event.clear()
            self.bar_event.set()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.bar_event.wait()            
            printBar()
            self.bar_event.clear()            
            self.foo_event.set()


if __name__ == '__main__':

    fb = FooBar(100)

    def printFoo():
        print("foo")

    def printBar():
        print("bar")

    def foo():
        fb.foo(printFoo)

    def bar():
        fb.bar(printBar)

    # init threads
    t1 = threading.Thread(target=bar)
    t2 = threading.Thread(target=foo)

    # start threads
    t1.start()
    t2.start()
    
    # join threads to the main thread
    t1.join()
    t2.join()