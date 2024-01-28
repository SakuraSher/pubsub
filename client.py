# client/client.py

import zmq
import middleware.PubSub as PubSub 

def start_client():
    context = zmq.Context()
    client_socket=context.socket(zmq.SUB)
    client_socket.connect("tcp://127.0.0.1:5555")
    #pubsub = PubSub.PubSub(context, "tcp://localhost:5555")

    while True:
        topic_filter = input("Enter topic to subscribe to (or '*' for all topics): ")
        client_socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

        while True:
            message = client_socket.recv_string()
            topic, content = message.split(' ', 1)
            print(f"Received message on topic '{topic}': {content}")

if __name__ == "__main__":
    start_client()
