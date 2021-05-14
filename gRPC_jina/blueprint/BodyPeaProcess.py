import zmq
import time
from  multiprocessing import Process,Manager
from  threading import Thread
from  PeaMeta import _get_event,_make_or_event,PeaType
'''
Body Pea is the Consumer in ZMQ Pull - Push model
'''

      
class Base(Process):
    """
    Inherit from Process and
    holds the zmq address.
    """
    def __init__(self,server_addr,client_addr):
        super().__init__()
        self.server_addr = server_addr
        self.client_addr = client_addr
        
class BodyPeas(Base):     
    def run(self):
        consumer_context = zmq.Context()
        # Connect with Producer
        consumer_receiver = consumer_context.socket(zmq.PULL)
        consumer_receiver.connect(server_addr)
        # Connect with Result Collector
        consumer_sender = consumer_context.socket(zmq.PUSH)
        consumer_sender.connect(client_addr)
    
        message = consumer_receiver.recv()
        # Body pea finished their job
        
        if message:
            print(message)
        print("Tasks finished!")
        consumer_sender.send_string(str(message, 'utf-8'))
        print("Send back message to gRPC Server")



if __name__ == "__main__":
    server_addr = 'tcp://127.0.0.1:2626'
    client_addr = 'tcp://127.0.0.1:3737'
    bodyPea = BodyPeas(server_addr, client_addr)
    bodyPea.start()