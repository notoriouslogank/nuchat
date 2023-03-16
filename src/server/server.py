import threading
import socket
import os
from config import host, port, admin_pwd, banner

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    """Send a message to all clients."""
    for client in clients:
        client.send(message)


def handle(client):
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
                    with open("bans.txt", "a") as f:
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

        with open("bans.txt", "r") as f:
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

        print(f" IP: {str(address)} \n Name: {nickname}. \n")
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
    print(banner())

print(f"Server is listening on IP {host}:{port}...")
print(banner())
receive()
