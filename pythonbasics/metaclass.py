def pythondemo():
    print("pythondemo")

from threading import Thread
from multiprocessing import Process
import threading


class Meta(type):
    def __new__(cls, name, bases, dct):
        print("name is ", name)
        bases = Process,
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        x.pythondemo = pythondemo

        return x

class HeadPea:
    pass

class TailPea:


class Pod:
    headPea: 
    tailPea:
    
    parallel = 4
    name = 'loader'
    peas = []
    for i in range(parallel):
        pea = Pea()
        pea.start()


class Pea(metaclass=Meta):
    def run(self):
       print('Started loading contents from file : ', threading.get_ident())
       Sentencizer(inputData)


if __name__ == "__main__":
    foo = Foo()
    foo.start()
    print("main process")
