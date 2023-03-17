import threading
import socket
import random
from datetime import datetime
import config


def welcome():
    """Take nickname, check it against database, print to client."""
    global nickname
    global password
    print("Choose a nickname.")
    print("If blank, a nickname will be randomly")
    print("assigned to you. \n")
    nickname = input("Nickname: ")

    '''Check the nickname for ADMIN or BAN; assign guest accout.'''
    if nickname == "":
        nickname = (
            f"{guests[random.randint(0,6)]}" + f"{str(random.randint(1000, 9999))}"
        )
        print("Your randomly generated nickname for this session is: ")
        print(f"{nickname}")

    if nickname == "ADMIN":
        password = input("Enter password for user ADMIN: ")

    print(banner(cyberpunk))


def prepare():
    """Allow the client connection and keep it open."""
    global client
    global stop_thread
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    stop_thread = False


def receive():
    while True:
        global stop_thread
        now = datetime.now()
        t = now.strftime("%H:%M:%S")
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
                next_message = client.recv(1024).decode("ascii")
                if next_message == "PASS":
                    client.send(password.encode("ascii"))
                    if client.recv(1024).decode("ascii") == "REFUSE":
                        print("Connection refused; incorrect login information.")
                        stop_thread = True
                elif next_message == "BAN":
                    print("Connection refused: BANNED!")
                    client.close()
                    stop_thread = True
            elif message.startswith(nickname):
                print("\n")
                continue
            else:
                print(t)
                print(message)
                print("")
        except:
            print("An error occurred.  Whoopsie-daisy!")
            client.close()
            break


def write():
    while True:
        if stop_thread:
            break
        message = f'{nickname}: {input("")}' + "\n"
        if message[len(nickname) + 2 :].startswith("!"):
            if nickname == "ADMIN":
                if message[len(nickname) + 2 :].startswith("!kick"):
                    client.send(f"KICK {message[len(nickname)+2+6:]}".encode("ascii"))
                elif message[len(nickname) + 2 :].startswith("!ban"):
                    client.send(f"BAN {message[len(nickname)+2+5:]}".encode("ascii"))
            else:
                print("This command can only be executed by ADMIN!")
        else:
            client.send(message.encode("ascii"))


def threads():
    """Start threads."""
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    write_thread = threading.Thread(target=write)
    write_thread.start()


def main():
    welcome()
    prepare()
    threads()


main()
