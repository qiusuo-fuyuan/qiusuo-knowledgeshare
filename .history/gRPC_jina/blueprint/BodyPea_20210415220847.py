import zmq
import time
import multiprocessing
import threading
'''
Body Pea is the Consumer in ZMQ Pull - Push model
'''

class PeaType(type):
    """Type of :class:`Pea`, metaclass of :class:`BasePea`."""
    _dct = {}
    
    def __new__(cls, name, bases, dct):
        """
        Create and register a new class with this meta class.

        :param name: name of the :class:`Pea`
        :param bases: bases of :class:`Pea`
        :param dct: arguments dictionary
        :return: registered class
        """
        _cls = super().__new__(cls, name, bases, dct)
        PeaType._dct.update({name: {'cls': cls,
                                    'name': name,
                                    'bases': bases,
                                    'dct': dct}})
        return _cls

    def __call__(self, *args, **kwargs) -> 'PeaType':
        """
        change runtime backend

        :param args: arguments
        :param kwargs: keyword arguments
        :return: Call self as a function.
        """
        # switch to the new backend
        _cls = multiprocessing.Process

        # rebuild the class according to mro
        for c in self.mro()[-2::-1]:
            arg_cls = PeaType._dct[c.__name__]['cls']
            arg_name = PeaType._dct[c.__name__]['name']
            arg_dct = PeaType._dct[c.__name__]['dct']
            _cls = super().__new__(arg_cls, arg_name, (_cls,), arg_dct)

        return type.__call__(_cls, *args, **kwargs)



class BodyPea:
    def __init__(self):
        consumer_context = zmq.Context()
        # Connect with Producer
        consumer_receiver = consumer_context.socket(zmq.PULL)
        consumer_receiver.connect('tcp://127.0.0.1:2626')
        # Connect with Result Collector
        consumer_sender = consumer_context.socket(zmq.PUSH)
        consumer_sender.connect('tcp://127.0.0.1:3737')

        message = consumer_receiver.recv()
        # Body pea finished their job
        if message:
            print(message)
        print("Tasks finished!")
        consumer_sender.send_string(str(message, 'utf-8'))
        print("Send back message to gRPC Server")


BodyPea()
