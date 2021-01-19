import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server5555…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(5):
    print("Sending request 5555%s …" % request)
    socket.send(b"Hello5555")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))







#  Socket to talk to server6666
print("Connecting to hello world server6666…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello6666")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))