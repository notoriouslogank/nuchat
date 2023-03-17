import threading
import socket
import os
import src
from datetime import datetime
from src import config, client, server
from src.config import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((config.getHost()))
server.listen()

clients = []
nicknames = []

def timestamp():
    time = datetime.now()
    now = time.strftime("%H:%M:%S")
    return str(now)

def broadcast(message):
    """Send a message to all clients."""
    for client in clients:
        print(f'{timestamp()}')
        client.send(message)


def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)
            print(timestamp())
            print(msg.decode("ascii"))
            if msg.decode("ascii").startswith("KICK"):
                if nicknames[clients.index(client)] == "ADMIN":
                    name_to_kick = msg.decode("ascii")[5:]
                    kick_user(name_to_kick)
                else:
                    client.send("Command refused; must be ADMIN!".encode("ascii"))
            elif msg.decode("ascii").startswith("BAN"):
                if nicknames[clients.index(client)] == "ADMIN":
                    name_to_ban = msg.decode("ascii")[4:]
                    kick_user(name_to_ban)
                    with open("src/server/bans.log", "a") as f:
                        f.write(f"{name_to_ban}\n")
                    print(f"{name_to_ban} was banned.")
                else:
                    client.send("Command refused; must be ADMIN!".encode("ascii"))          
            elif msg.decode("ascii").starswith("CLS"):
                    system.os('clear')
                    print(banner())
            else:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat.".encode("ascii"))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connection from: {str(address)}.")

        client.send("NICK".encode("ascii"))

        nickname = client.recv(1024).decode("ascii")

        with open("src/server/bans.log", "r") as f:
            bans = f.readlines()

        if nickname + "\n" in bans:
            client.send("BAN".encode("ascii"))
            client.close()
            continue

        if nickname == "ADMIN":
            client.send("PASS".encode("ascii"))
            password = client.recv(1024).decode("ascii")

            if password != admin_pwd:
                client.send("REFUSE".encode("ascii"))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        client.send("Successfully connected to the server. \n".encode("ascii"))
        broadcast(f"{nickname} joined the chat. \n".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send("You were kicked by ADMIN!".encode("ascii"))
        nicknames.remove(name)
        broadcast(f"{name} was kicked by ADMIN!".encode("ascii"))

def cls():
    os.system(clear)
    print(welcome_banner())

print(f"Server is listening on IP {config.host}:{config.port}...")
#print(welcome_banner())
receive()
