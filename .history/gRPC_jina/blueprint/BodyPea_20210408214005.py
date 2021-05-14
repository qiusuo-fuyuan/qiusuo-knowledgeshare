import zmq
import time

'''
Body Pea is the Consumer in ZMQ Pull - Push model
'''


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
