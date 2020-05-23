#!/usr/bin/env python3
import json
from json import JSONEncoder
import jsonpickle
import enum

class Scheduler:
    ready: Process = []
    waiting: Process = []

    @staticmethod
    def schedule():
        ready[0].run()

class File:
    buffer = []
    def readSync(self):
        """ read from disk and store into buffer"""
        if buffer.length == 0:
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
    currentExecuteCommand: None

    def run(self):
        """load address currentExecuteCommand value to cpu"""

class Socket:
    buffer = []
    port = None
    source = None
    target = None
    interface = None
    process: Process
    def read(self):
        """ read from disk and store into buffer"""
    
    def write(self):
        """take data from user space and write to disk"""



class HttpMethod:
   GET = 1
   POST = 2

class RequestURL:
    RNN_TRAIN = "/rnn/train"
    RNN_PREDICT = "rnn/predict"

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
