class Foo:
    def __init__(self):
        pass

    def first(self, printFirst):
        """Call the printFirst function."""
        printFirst()

    def second(self, printSecond):
        """Call the printSecond function."""
        printSecond()

    def third(self, printThird):
        """Call the printThird function."""
        printThird()

import threading

def print_first():
    print("first")

def print_second():
    print("second")

def print_third():
    print("third")

foo = Foo()

threads = [
    threading.Thread(target=foo.first, args=(print_first,)),
    threading.Thread(target=foo.second, args=(print_second,)),
    threading.Thread(target=foo.third, args=(print_third,))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
