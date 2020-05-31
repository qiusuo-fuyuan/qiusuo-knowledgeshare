#!/usr/bin/env python3
import json
from json import JSONEncoder
import jsonpickle
import enum

class Scheduler:
    ready = []
    waiting = []

    @staticmethod
    def schedule():
        ready[0].run()

class File:
    buffer = []
    def readSync(self): 
        """ read from disk and store into buffer"""
        if buffer.length == 0:
            """send command to disk to read content, this will be executed by the file system driver"""
            """add current process to wait list"""
            Scheduler.schedule()
    
    def readASync(self):
        """ read from disk and store into buffer"""
        if buffer.length == 0:
            return

    def write(self):
        """take data from user space and write to disk"""

class Process:
    files = []
    sockets = []
    threads = []

    def run(self):
        """load address currentExecuteCommand value to cpu"""

class Socket:
    buffer = []
    Listeningport = None
    TargetPort = None
    sourceAddress = None
    targetAddress = None
    interface = None
    prcess: Process = None
    def read(self):
        """ read from disk and store into buffer"""
    
    def write(self):
        """take data from user space and write to disk"""


class HttpMethod:
   GET = 1
   POST = 2

class RequestURL:
    RNN_TRAIN = "/rnn/train"
    RNN_PREDICT = "/rnn/predict"

class HttpProtocol:
    method: HttpMethod
    url: RequestURL
    message = None

    def __init__(self,method,url,message):
        self.method = method
        self.url = url
        self.message = message

class HttpProtocolEncoder(JSONEncoder):
    def default(self, o):
            return o.__dict__



def lookupSocket(targetPort, targetInterface):
    """Get the socket which has the same target port and target interface"""

def serialize(httpRequest):
    httpProtocolJson = jsonpickle.encode(httpRequest, unpicklable=True)
    return json.dumps(httpProtocolJson, indent=4)

def deserialize(jsonString):
    httpProtocolJson = jsonpickle.decode(jsonString)
    httpProtocolDict = json.loads(httpProtocolJson)
    return HttpProtocol(httpProtocolDict['method'],httpProtocolDict['url'],httpProtocolDict['message'])
