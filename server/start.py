import os
import socket
import threading
from datetime import datetime

host = ()  # Server IP
port = ()  # Server Port
banlist = "server/banlist.txt"  # Where to save the list of banned users <./server/banlist.txt>

clients = []
nicknames = []


def getHost():
    """Automatically configure IP"""

    global host
    global port
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    port = 65522  # TODO: Is this best practices?
    hostname = host, port
    s.close()
    return hostname


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((getHost()))
server.listen()


def timestamp():
    """Return an ascii encoded, formatted string with current datetime for user as timestamp."""
    time = datetime.now()
    now = time.strftime("%H:%M:%S")
    return str(now)


def broadcast(message):
    """Send a message to all clients."""
    for client in clients:
        client.send(message)


def respond(client):
    """Decode the client message"""
    while True:
        try:
            msg = message = client.recv(1024)
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
                    with open(f"{banlist}", "a") as f:
                        f.write(f"{name_to_ban}\n")
                    print(f"{name_to_ban} was banned.")
                else:
                    client.send("Command refused; must be ADMIN!".encode("ascii"))
            elif msg.decode("ascii").startswith("CLS"):
                if nicknames[clients.index(client)] == "ADMIN":
                    os.system("clear")
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat.".encode("ascii"))
            nicknames.remove(nickname)
            break


def auth_connection():
    while True:
        client, address = server.accept()
        print(f"Connection from: {str(address)}.")
        nickname = client.recv(1024).decode("ascii")

        with open(f"{banlist}", "r") as f:
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

        thread = threading.Thread(target=respond, args=(client,))
        thread.start()


def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send("You were kicked by ADMIN!".encode("ascii"))
        nicknames.remove(name)
        broadcast(f"{name} was kicked by ADMIN!".encode("ascii"))


print(f"Server is auth_connection on IP {host}:{port}...\n")

auth_connection()
