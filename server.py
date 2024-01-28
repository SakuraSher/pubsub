# server/server.py


import zmq


import middleware.PubSub as PubSub 
def start_server():
    context = zmq.Context()
    pubsub =  PubSub.PubSub(context, "tcp://*:5555")

    while True:
        topic = input("Enter topic: ")
        message = input("Enter message: ")
        pubsub.publish(topic, message)

if __name__ == "__main__":
    start_server()
