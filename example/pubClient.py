from socket import socket
from AsyncSocketPubSub.client import PubSubClient

ADDRESS = "127.0.0.1"
PORT = 18883
ID = "Publisher"
CHANNEL = "C"
# DATA = "hello"
DATA = {"int": 1, "str": "hello", "float": 1.3, "list": ["a", 2]}

psClient = PubSubClient(
    serverAddress = ADDRESS,
    serverPort = PORT,
    id = ID
)

psClient.connect(socketClient = socket())

psClient.publish(
    channel = CHANNEL,
    payload = DATA
)
