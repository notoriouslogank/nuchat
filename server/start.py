import socket
import threading

HEADER = 2048
FORMAT = "ascii"
DISCONNECT_MSG = "!quit"
HOST = ()
PORT = ()
ADDR = ()


def hostInfo():
    """Automatically configure IP"""
    global HOST
    global PORT
    global ADDR
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    HOST = s.getsockname()[0]
    PORT = 65522  # TODO: Is this best practices?
    ADDR = HOST, PORT
    s.close()
    return ADDR


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(hostInfo())


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
                conn.close()
            print(f"[{addr}] {msg}")


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}.")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] Server is starting up.")
start()
