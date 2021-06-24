import zmq
import time
import os
from multiprocessing import Process, Manager
from threading import Thread
from PeaMeta import PeaType
import argparse
from myExec import MyExecutor
import yaml

"""
Body Pea is the Consumer in ZMQ Pull - Push model
"""


class BodyPea(metaclass=PeaType):
    def __init__(self, args: "argparse.Namespace"):
        super().__init__()

    def run(self):
        exec = yaml.load(
            open("yaml/myexec.yml"),
            Loader=yaml.Loader,
        )
        exec.execute()

    def __enter__(self):
        super().start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# BodyPea(Process).run()
# BodyPeas  -->  BodyPea  -->   PeaType --> __new__
# bodyPeas() ->  PeaType __call__