from __future__ import print_function
import logging

import grpc

from .generated import jina_pb2
from .generated import jina_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = jina_pb2_grpc.JinaStub(channel)
        response = stub.Reply(
            jina_pb2.JinaRequest(
                message=u"Message from grpc server! Let the body pea work!"
            )
        )
    print("Jina client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()