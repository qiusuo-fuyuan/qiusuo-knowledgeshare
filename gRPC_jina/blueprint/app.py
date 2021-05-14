# app.py
from concurrent import futures
import zmq
import grpc
from .generated import jina_pb2_grpc
from .grpc import Jinaer


class Server:
    @staticmethod
    def run():
        print("gRPC Server (ZMQ Client) Ready!")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        jina_pb2_grpc.add_JinaServicer_to_server(Jinaer(), server)
        server.add_insecure_port("[::]:50051")
        server.start()
        print("ZMQ Result Collector Ready!")
        context = zmq.Context()
        results_receiver = context.socket(zmq.PULL)
        results_receiver.bind("tcp://127.0.0.1:3333")
        message_from_consumer = results_receiver.recv()
        if message_from_consumer:
            print("Already received the message from Consumer (BodyPea)")
        server.wait_for_termination()
