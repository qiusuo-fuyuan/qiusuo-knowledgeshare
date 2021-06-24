from .generated import jina_pb2, jina_pb2_grpc
import zmq
import sys

# The gRPC Server


class Jinaer(jina_pb2_grpc.JinaServicer):
    def Reply(self, requst, context):
        """
        gRPC Server is the server of gRPC
        gRPC Server is the client of ZMQ (Client - Server Model)
        gRPC Server is the result collector of ZMQ (Pull - Push Model)
        """
        # Set up ZMQ Push/Pull Communication:
        # Result Collector: 3737
        # print("ZMQ Result Collector Ready!")
        print("grpcServer received message:" + requst.message)
        context = zmq.Context()
        results_receiver = context.socket(zmq.PULL)
        results_receiver.bind("tcp://127.0.0.1:3737")

        # Set up ZMQ Client/Server communication
        # Client:
        port = "1515"
        context = zmq.Context()
        # print("gRPC Server(ZMQ Client): Connecting to ZMQ Server(Head Pea)...")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:%s" % port)

        # print("gRPC Server(ZMQ Client): sending request to ZMQ Server(Head Pea)")
        socket.send_string(requst.message)
        # If receive a message from server, then we know that the request has
        # sent to the Head Pea, and peas are working
        # We need to set up the receiver of Pull Push model
        message_from_server = results_receiver.recv()
        if message_from_server:
            print(message_from_server)
        # Send the message back to gRPC Client that the mission is completed
        return jina_pb2.JinaReply(
            message="The mission assigned to pea is completed" + requst.message
        )
