import threading
import socket
import os
from datetime import datetime

host = ()
port = ()
clients = []
nicknames = []
banlist = 'server/banlist.txt'
def getHost():
    """
    Get IP and Port of server.

    """
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
                    with open(f'{banlist}', "a") as f:
                        f.write(f"{name_to_ban}\n")
                    print(f"{name_to_ban} was banned.")
                else:
                    client.send("Command refused; must be ADMIN!".encode("ascii"))          
            elif msg.decode("ascii").startswith("CLS"):
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
        nickname = client.recv(1024).decode("ascii")

        with open(f'{banlist}', "r") as f:
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

print(f"Server is listening on IP {host}:{port}...")
receive()
#print(welcome_banner())

""" banner1 = []
banner2 = []
banners = [banner1,
           banner2
           ]

# TODO: STATIC/DYNAMIC BANNER FLAG
def welcome_banner():
    banner = banners[1]
    #seed = random.randint(0, (len(fonts) - 1))
    #font = fonts[seed]
    for lines in banner:
        print(lines)
 """
