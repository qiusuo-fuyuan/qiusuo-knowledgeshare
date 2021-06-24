import zmq
import time
from multiprocessing import Process
import threading
from PeaMeta import PeaType, _get_event

"""
The HeadPea is the Producer in ZMQ Push - Pull model
The HeadPea is the Server in ZMQ Client - Server model
"""


class Headpeas(metaclass=PeaType):
    def __init__(self, args):
        super().__init__()
        self.is_ready = _get_event(self)
        self.is_shutdown = _get_event(self)
        """
        self.args = args
        self.name = self.args.name or self.__class__.__name__
          """

    def run(self):
        # Initialization in ZMQ for Server in Client - Server
        server_context = zmq.Context()
        server_socket = server_context.socket(zmq.REP)
        server_socket.bind("tcp://127.0.0.1:1515")
        server_message = server_socket.recv()
        if server_message:
            print(server_message)

        # Initialization in ZMQ for Producer
        producer_context = zmq.Context()
        producer_socket = producer_context.socket(zmq.PUSH)
        producer_socket.bind("tcp://127.0.0.1:2626")
        self.is_ready.set()
        print("Event is set")
        # Send the message to the consumer
        producer_socket.send_string(str(server_message, "utf-8"))

    def __enter__(self):
        super().start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


# Headpeas(Process).run()
