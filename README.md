# AsyncSocketPubSub

This module provides Pub/Sub based communication using socket communication.

## Requirement

This module requires the [`pubsub`](https://github.com/nehz/pubsub) module:

```shell
pip install pubsub
```

## Usage

directory structure:

```shell
┋
┣ AsyncSocketPubSub
┣ xxx.py
┋
```

see [examples](https://github.com/amenaruya/AsyncSocketPubSub/tree/main/example)

### Simple using

Use `threading` for publisher and subscriber when using `pubsub` module.

```python
from AsyncSocketPubSub.server import PubSubClients
from threading import Thread
import time

# similar to topic in MQTT
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

# thread
sub = Thread(
    target = Subscriber,
    daemon = True
)
sub.start()

Publisher()

```

### Server and Client
