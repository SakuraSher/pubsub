# common/pubsub_utils.py

import zmq

class PubSub:
    def __init__(self, context, bind_address):
        self.socket = context.socket(zmq.PUB)
        self.socket.bind(bind_address)

    def publish(self, topic, message):
        self.socket.send_string(f"{topic} {message}")
