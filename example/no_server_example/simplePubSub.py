from AsyncSocketPubSub.server import PubSubClients
from threading import Thread
import time

CHANNEL = "C"

def Subscriber():
    subClient = PubSubClients(id = "subscriber")
    while True:
        data = subClient.subscribe(channel = CHANNEL)
        print(data)

def Publisher():
    pubClient = PubSubClients(id = "publisher")
    while True:
        pubClient.publish(
            channel = CHANNEL,
            payload = "hello"
        )
        time.sleep(3)

sub = Thread(
    target = Subscriber,
    daemon = True
)
sub.start()

Publisher()
