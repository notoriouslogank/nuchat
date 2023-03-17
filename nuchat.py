"""The so-called main file."""
import os
import threading
import socket
import random
import server.start

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
