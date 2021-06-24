import yaml
import zmq


class MyExecutor(yaml.YAMLObject):
    yaml_tag = u"!MyExecutor"

    def execute(self):
        consumer_context = zmq.Context()
        # Connect with Producer
        consumer_receiver = consumer_context.socket(zmq.PULL)
        consumer_receiver.connect("tcp://127.0.0.1:2626")
        # self.is_ready.set()
        # Connect with Result Collector
        consumer_sender = consumer_context.socket(zmq.PUSH)
        consumer_sender.connect("tcp://127.0.0.1:3737")
        message = consumer_receiver.recv()
        # Body pea finished their job

        if message:
            print("bodypea received %s" % message)
        print("Tasks finished!")
        consumer_sender.send_string(str(message, "utf-8"))
        print("Send back message to gRPC Server")

    # def __repr__(self):
    #     return "%s" % self.__class__.__name__


# print(yaml.dump(MyExecutor()))
