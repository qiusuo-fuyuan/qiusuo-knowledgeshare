import zmq
import time
import os
from multiprocessing import Process, Manager
from threading import Thread
from PeaMeta import PeaType, _get_event, _make_or_event
import argparse

"""
Body Pea is the Consumer in ZMQ Pull - Push model
"""


class BodyPea(metaclass=PeaType):
    def __init__(self, args: "argparse.Namespace"):
        super().__init__()
        '''
        self.args = args
        self.is_ready = _get_event(self)
        self.is_shutdown = _get_event(self)
        self.ready_or_shutdown = _make_or_event(self, self.is_ready, self.is_shutdown)
        self.name = self.args.name or self.__class__.__name__
        '''

    def run(self):
        consumer_context = zmq.Context()
        # Connect with Producer
        consumer_receiver = consumer_context.socket(zmq.PULL)
        consumer_receiver.connect("tcp://127.0.0.1:2626")
        # self.is_ready.set()
        # Connect with Result Collector
        consumer_sender = consumer_context.socket(zmq.PUSH)
        consumer_sender.connect("tcp://127.0.0.1:3737")
        message = consumer_receiver.recv()
        # Body pea finished their job

        if message:
            print(message)
        print("Tasks finished!")
        consumer_sender.send_string(str(message, "utf-8"))
        print("Send back message to gRPC Server")

    def __enter__(self):
        super().start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# BodyPea(Process).run()
# BodyPeas  -->  BodyPea  -->   PeaType --> __new__

# bodyPeas() ->  PeaType __call__