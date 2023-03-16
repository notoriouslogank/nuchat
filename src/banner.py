import random

wizard = [
    "::::::::  :::    :::     ::: ::::::::::: ::::::::::: :::::::::: :::::::::  :::::::::   ::::::::  :::    ::: ",
    ":+:    :+: :+:    :+:   :+: :+:   :+:         :+:     :+:        :+:    :+: :+:    :+: :+:    :+: :+:    :+: ",
    "+:+        +:+    +:+  +:+   +:+  +:+         +:+     +:+        +:+    +:+ +:+    +:+ +:+    +:+  +:+  +:+  ",
    "+#+        +#++:++#++ +#++:++#++: +#+         +#+     +#++:++#   +#++:++#:  +#++:++#+  +#+    +:+   +#++:+   ",
    "+#+        +#+    +#+ +#+     +#+ +#+         +#+     +#+        +#+    +#+ +#+    +#+ +#+    +#+  +#+  +#+  ",
    "#+#    #+# #+#    #+# #+#     #+# #+#         #+#     #+#        #+#    #+# #+#    #+# #+#    #+# #+#    #+# ",
    " ########  ###    ### ###     ### ###         ###     ########## ###    ### #########   ########  ###    ### ",
]

cyberpunk = [
    " _______ _     _ _______ _______ _______ _______ ______  ______  _______ _     _ ",
    "(_______|_)   (_|_______|_______|_______|_______|_____ \(____  \(_______|_)   (_)",
    " _       _______ _______    _       _    _____   _____) )____)  )_     _   ___   ",
    "| |     |  ___  |  ___  |  | |     | |  |  ___) |  __  /|  __  (| |   | | |   |  ",
    "| |_____| |   | | |   | |  | |     | |  | |_____| |  \ \| |__)  ) |___| |/ / \ \ ",
    " \______)_|   |_|_|   |_|  |_|     |_|  |_______)_|   |_|______/ \_____/|_|   |_|",
]

blewd = [
    "@@@@@@@ @@@  @@@  @@@@@@  @@@@@@@ @@@@@@@ @@@@@@@@ @@@@@@@  @@@@@@@   @@@@@@  @@@  @@@",
    "@@      @@!  @@@ @@!  @@@   @@!     @@!   @@!      @@!  @@@ @@!  @@@ @@!  @@@ @@!  !@@",
    "@!      @!@!@!@! @!@!@!@!   @!!     @!!   @!!!:!   @!@!!@!  @!@!@!@  @!@  !@!  !@@!@! ",
    "!!      !!:  !!! !!:  !!!   !!:     !!:   !!:      !!: :!!  !!:  !!! !!:  !!!  !: :!! ",
    ":: :: :  :   : :  :   : :    :       :    : :: :::  :   : : :: : ::   : :. :  :::  :::",
]

askew = [
    "________________/\\\__________________________________________________________________________________/\\\____________________________________        ",
    " _______________\/\\\_________________________________________________________________________________\/\\\____________________________________       ",
    "  _______________\/\\\____________________________/\\\__________/\\\___________________________________\/\\\____________________________________      ",
    "   _____/\\\\\\\\_\/\\\__________/\\\\\\\\\_____/\\\\\\\\\\\__/\\\\\\\\\\\_____/\\\\\\\\___/\\/\\\\\\\__\/\\\____________/\\\\\_____/\\\____/\\\_     ",
    "    ___/\\\//////__\/\\\\\\\\\\__\////////\\\___\////\\\////__\////\\\////____/\\\/////\\\_\/\\\/////\\\_\/\\\\\\\\\____/\\\///\\\__\///\\\/\\\/__    ",
    "     __/\\\_________\/\\\/////\\\___/\\\\\\\\\\_____\/\\\_________\/\\\_______/\\\\\\\\\\\__\/\\\___\///__\/\\\////\\\__/\\\__\//\\\___\///\\\/____   ",
    "      _\//\\\________\/\\\___\/\\\__/\\\/////\\\_____\/\\\_/\\_____\/\\\_/\\__\//\\///////___\/\\\_________\/\\\__\/\\\_\//\\\__/\\\_____/\\\/\\\___  ",
    "       __\///\\\\\\\\_\/\\\___\/\\\_\//\\\\\\\\/\\____\//\\\\\______\//\\\\\____\//\\\\\\\\\\_\/\\\_________\/\\\\\\\\\___\///\\\\\/____/\\\/\///\\\_ ",
    "        ____\////////__\///____\///___\////////\//______\/////________\/////______\//////////__\///__________\/////////______\/////_____\///____\///__",
]

toybox = [
    " ______  ___   ___  ________  _________ _________ ______  ______    _______  ______  __     __     ",
    "/_____/\/__/\ /__/\/_______/\/________//________//_____/\/_____/\ /_______/\/_____/\/__/\ /__/\    ",
    "\:::__\/\::\  \\  \ \::: _  \ \__.::.__ \\__.::.__ \\::::_\/\:::_ \ \\::: _   \ \:::_ \ \  \::\:.\ \   ",
    " \:\ \  _\::\/_\ .\ \::(_)  \ \ \::\ \    \::\ \  \:\/___/\:(_) ) )\::(_)  \/\:\ \ \ \_ \::_\:_\/   ",
    "  \:\ \/_/\:: ___::\ \:: __  \ \ \::\ \    \::\ \  \::___\/\: __ `\ \::  _  \ \:\ \ \  \_\/__\_\_/\ ",
    "   \:\_\ \ \: \  \\::\ \:.\ \  \ \ \::\ \    \::\ \  \:\____/\ \ `\ \ \::(_)  \ \:\_\ \  \ \ \ \::\ \\",
    "    \_____\/\__\/ \::\/\__\/\__\/  \__\/     \__\/   \_____\/\_\/ \_\/\_______\/\_____\/\_\/  \__\/",
    "                                                                                                   ",
]

trek = [
    "     dBBBP  dBP dBP dBBBBBb  dBBBBBBP dBBBBBBP dBBBP dBBBBBb   dBBBBb   dBBBB`Bb  .BP",
    "                         BB                              dBP      dBP  dBP.BP    .BP ",
    "   dBP    dBBBBBP    dBP BB   dBP      dBP   dBBP    dBBBBK   dBBBK   dBP.BP   dBBK  ",
    "  dBP    dBP dBP    dBP  BB  dBP      dBP   dBP     dBP  BB  dB  db  dBP.BP   dB     ",
    " dBBBBP dBP dBP    dBBBBBBB dBP      dBP   dBBBBP  dBP  dB  dBBBBP  dBBBBP   dB  dBP ",
]

chic = [
    "            88                                                                88                                    ",
    "            88                         ,d       ,d                            88                                    ",
    "            88                         88       88                            88                                    ",
    " ,adPPYba,  88,dPPYba,   ,adPPYYba,  MM88MMM  MM88MMM  ,adPPYba,  8b,dPPYba,  88,dPPYba,    ,adPPYba,  8b,     ,d8  ",
    "a8          88P      8a         `Y8    88       88    a8Pooooo88  88P     Y8  88P      8a  a8       8a  `Y8, ,8P    ",
    "8b          88       88  ,adPPPPP88    88       88    8PP^^^^^^   88          88       d8  8b       d8    )888(     ",
    '"8a,   ,aa  88       88  88,    ,88    88,      88,    8b,   ,aa  88          88b,   ,a8    8a,   ,a8   ,d8  8b,    ',
    '   Ybbd8    88       88   "8bbdP Y8     Y888     Y888    Ybbd8    88          8Y  Ybbd8      YbbdP     8P      Y8    ',
]

fonts = [
    wizard,
    askew,
    chic,
    cyberpunk,
    blewd,
    toybox,
    trek,
]


def banner():
    seed = random.randint(0, (len(fonts) - 1))
    print(f"{seed}")
    font = fonts[seed]
    for lines in font:
        print(lines, end="\n")


banner()
