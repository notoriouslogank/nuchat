import socket
import threading

HEADER = 2048
FORMAT = 'ascii'
SERVER = '192.168.0.238'
PORT = 65522
ADDR = (SERVER, PORT)
DISCONNECT_MSG = '!quit'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
while True:
    send(input())