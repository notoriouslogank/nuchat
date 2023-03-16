import socket
import random

host = ()
port = 65522  # TODO: Is this best practices?

def getHost():
    """
    Get IP and Port of server.

    """
    global host
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()

getHost()

# TODO: Toggle switch for ALLOW-GUESTS-WITHOUT-NICKNAME
""" List of nicks for guest accounts """
guests = [
    "guest",
    "ghost",
    "kirk",
    "redshirt",
    "klingon",
    "vulcan",
    "romulan",
    "break",
    "pissflaps",
    "blackpenislover",
    "cockknocker",
    "dicklips",
    "shrekislove",
    "shrekislife",
    "gaylord",
    "faggot_but_with_a_ph",
    "useless",
    "generic",
    "noname",
    "blurryface",
    "blank",
]

admin_pwd = "mutatismutandis"  # TODO: Obfuscate this password

banner1 = []
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
