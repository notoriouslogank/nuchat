import socket
import threading

host = ("192.168.0.238", 65522)
stop_thread = False


def usr_acct():
    """Take nickname, check it against database, print to client."""
    global nickname
    global password

    print("Choose a nickname.")
    print("If blank, a nickname will be randomly")
    print("assigned to you. \n")
    nickname = input("Nickname: ")

    if nickname == "ADMIN":
        password = input("Enter password for user ADMIN: ")


def usr_online():
    """Allow the client connection and keep it open."""
    global client
    global stop_thread
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(host)

    stop_thread = False


def response():
    while True:
        global stop_thread
        global client
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode("ascii")
            if message == "KICK":
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
            else:
                print(f"{nickname} : {message}")
                print("")
        except:
            print("An error occurred.  Whoopsie-daisy!")
            stop_thread = True
            client.close()
            break


def command():
    """ Commands
    
    # TODO: This could probably be made into a class relatively easily, eh?  Possibly move it into its own 'commands' module.
    """
    global nickname
    global stop_thread
    while True:
        if stop_thread:
            break
        message = f'{nickname}: {input(" ")} \n'
        if message[len(nickname) + 2 :].startswith("!"):
            if message[len(nickname) + 2 :].startswith('!quit'):
                print("Goodbye!")
                client.close()
                stop_thread = True
                break
            elif nickname == "ADMIN":
                if message[len(nickname) + 2 :].startswith("!kick"):
                    client.send(f"KICK {message[len(nickname)+2+6:]}".encode("ascii"))
                elif message[len(nickname) + 2 :].startswith("!ban"):
                    client.send(f"BAN {message[len(nickname)+2+5:]}".encode("ascii"))
            else:
                print("This command can only be executed by ADMIN!")
        else:
            client.send(message.encode("ascii"))
            print('\n')


def main():
    usr_acct()
    usr_online()
    response_thread = threading.Thread(target=response)
    response_thread.start()
    write_thread = threading.Thread(target=command)
    write_thread.start()


main()
