from socket import socket
from AsyncSocketPubSub.client import PubSubClient

ADDRESS = "127.0.0.1"
PORT = 18883
ID = "Subscriber"
CHANNEL = "C"

psClient = PubSubClient(
    serverAddress = ADDRESS,
    serverPort = PORT,
    id = ID
)

psClient.connect(socketClient = socket())

psClient.subscribe(CHANNEL)
