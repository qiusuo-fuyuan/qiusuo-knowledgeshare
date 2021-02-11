import zmq
import time

'''
The HeadPea is the Producer in ZMQ Push - Pull model
The HeadPea is the Server in ZMQ Client - Server model
'''
def HeadPea():
    # Initialization in ZMQ for Server in Client - Server
    server_context = zmq.Context()
    server_socket = server_context.socket(zmq.REP)
    server_socket.bind("tcp://127.0.0.1:1515")
    server_message = server_socket.recv()
    if server_message:
        print("Already received the requect from gRPC Server, sending message to Body Pea")

    # Initialization in ZMQ for Producer
    producer_context = zmq.Context()
    producer_socket = producer_context.socket(zmq.PUSH)
    producer_socket.bind("tcp://127.0.0.1:2626")

    # Send the message to the consumer
    producer_socket.send_string("Body peas, Please begin your work right now!")
    return 

HeadPea()