# Aqui guardamos los datos
letras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N",
          13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K", 22: "E"}

mazo = {}

players = {}
first_players = {"players":[]}
delete_players = {}

cardgame = {'cardgame_id': 0, 'players': 0, 'start_hour': 0,
            'rounds': 0, 'end_hour': 0, 'deck_id': 0}

player_game_toDB = {}
current_round = {"round":0}
player_game_round = {}


context_game = {"game": [], "mazo": [], "rounds": 5}

deck_on_game = {"deck":1}

menu_principal = ("*" * 140) + "\n" + (" " * 37) + \
                 "_____                         ___              __   __  __      ______" + (" " * 33) + "\n" + \
                 (" " * 36) + \
                 "/ ___/___ _   _____  ____     /   |  ____  ____/ /  / / / /___ _/ / __/" + "\n" + (" " * 36) + \
                 "\__ \/ _ \ | / / _ \/ __ \   / /| | / __ \/ __  /  / /_/ / __ `/ / /" + "\n" + (" " * 35) + \
                 "___/ /  __/ |/ /  __/ / / /  / ___ |/ / / / /_/ /  / __  / /_/ / / __/" + "\n" + (" " * 34) + \
                 "/____/\___/|___/\___/_/ /_/  /_/  |_/_/ /_/\__,_/  /_/ /_/\__,_/_/_/" + "\n\n" + ("*" * 140) + \
                 "\n\n" + "1)Add/Remove/Show Players\n".rjust(80) + "2)Settings\n".rjust(65) + \
                 "3)Play Game\n".rjust(66) + "4)Ranking\n".rjust(64) + "5)Reports\n".rjust(64) + "6)Exit".rjust(60)
menu_principal_opt = ('1', '2', '3', '4', '5', '6')

menu_01 = ("*" * 140) + "\n" + (" " * 49) + "____   __\n" + \
          (" " * 48) + "/ __ \ / /____ _ __  __ ___   _____ _____\n" + (" " * 47) + \
          "/ /_/ // // __ `// / / // _ \ / ___// ___/\n" + (" " * 46) + \
          "/ ____// // /_/ // /_/ //  __// /    \__\ \n" + (" " * 45) + \
          "/_/    /_/ \__,_/ \__, / \___//_/   /____/\n" + \
          (" " * 62) + "/____/" + "\n" + ("*" * 140) + "\n\n" + "1)New Human Player\n".rjust(73) + \
          "2)New Boot\n".rjust(65) + "3)Show/Remove Players\n".rjust(76) + "4)Go back\n".rjust(64)
menu_01_opt = ('1', '2', '3', '4')

menu_02 = ("*" * 140) + "\n" + "".ljust(40) + ".d8888b.          888    888    d8b\n" + \
        "".ljust(39) + "d88P  Y88b         888    888    Y8P\n" + \
        "".ljust(39) + "Y88b.              888    888\n" +\
        "".ljust(39) + "  Y888b.   .d88b.  888888 888888 888 88888b.   .d88b.  .d8888b\n" + \
        "".ljust(42) + " Y88b. d8P  Y8b 888    888    888 888  88b d88P 88b 88K\n" + \
        "".ljust(43) + "  888 88888888 888    888    888 888  888 888  888  Y8888b.\n" + \
        "".ljust(38) + "Y88b  d88P Y8b.     Y88b.  Y88b.  888 888  888 Y88b 888      X88\n" + \
        "".ljust(39) + " Y8888P    Y8888    Y888   Y888  888 888  888   Y88888  88888P\n" + \
        "".ljust(90) + "888\n" + \
        "".ljust(85) + "Y8b d88P\n" + \
        "".ljust(87) + "Y88P\n\n" + ("*" * 140) + "\n\n" + "1)Set Game Players\n".rjust(73) + \
        "2)Set Card's Deck\n".rjust(72) + "3)Set Max Rounds(Default 5 Rounds)\n".rjust(89) + "4)Go back".rjust(63)
menu_02_opt = ('1', '2', '3', '4')

menu_04 = ("*" * 140) + "\n" + ("*" * 140) + "\n\n" + "1)Players with more earnings\n".rjust(83) + \
          "2)Players with more games played\n".rjust(87) + \
          "3)Players with more minuts played\n".rjust(88) + \
          "4)Go back\n".rjust(64)
menu_04_opt = ('1', '2', '3', '4')

menu_05 = ("*" * 140) + "\n" + \
          ("*" * 140) + "\n\n" + "1)  Initial card more repeated by each user,\n".rjust(94) + \
          "only users who have played a minimum of 3 games.\n".rjust(102) + \
          "2)  Player who makes the highest bet per game,\n".rjust(96) + \
          "find the round with the highest bet.\n".rjust(90) + \
          "3)  Player who makes the lowest bet per game.\n".rjust(95) + \
          "4)  Percentage of rounds won per player in each game\n".rjust(102) + \
          "(%), as well as their average bet for the game.\n".rjust(101) + \
          "5)  List of games won by Bots.\n".rjust(80) + \
          "6)  Rounds won by the bank in each game.\n".rjust(90) + \
          "7)  Number of users have the bank in each game.\n".rjust(97) + \
          "8)  Average bet per game.\n".rjust(75) + \
          "9)  Average bet of the first round of each game.\n".rjust(98) + \
          "10)  Average bet of the las round of each game.\n".rjust(96) + \
          "11)  Go back\n".rjust(61)
menu_05_opt = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')

players_banner = ("*" * 140) + "\n" + (" " * 49) + "____   __\n" + \
                 (" " * 48) + "/ __ \ / /____ _ __  __ ___   _____ _____\n" + (" " * 47) + \
                 "/ /_/ // // __ `// / / // _ \ / ___// ___/\n" + (" " * 46) + \
                 "/ ____// // /_/ // /_/ //  __// /    \__\ \n" + (" " * 45) + \
                 "/_/    /_/ \__,_/ \__, / \___//_/   /____/\n" + \
                 (" " * 62) + "/____/" + "\n" + ("*" * 140) + "\n\n"

menu_022 = ("*" * 140) + "\n" + (" " * 34) + \
          "____               __      ____   ____   ______                  __" + (" " * 30) + "\n" + \
          (" " * 30) + \
          "   / __ \ ___   _____ / /__   / __ \ / __/  / ____/____ _ _____ ____/ /_____" + "\n" + (" " * 30) + \
          "  / / / // _ \ / ___// //_/  / / / // /_   / /    / __ `// ___// __  // ___/" + "\n" + (" " * 30) + \
          " / /_/ //  __// /__ / ,<    / /_/ // __/  / /___ / /_/ // /   / /_/ /(__  )" + "\n" + (" " * 30) + \
          "/_____/ \___/ \___//_/|_|   \____//_/     \____/ \__,_//_/    \__,_//____/" + "\n\n" + ("*" * 140) + \
          "\n\n" + "1) ESP - ESP(DEFAULT)\n".rjust(76) + \
          "2) POK - POK\n".rjust(67) + "0) Go back".rjust(64)
menu_022_opt = ('1', '2', '0')

menu_ingame = "1)Set bet\n".rjust(74) + \
              "2)Order card\n".rjust(67) + \
              "3)Next turn\n".rjust(66) + \
              "4)Show stats\n".rjust(67) + \
              "5)Autoplay".rjust(64)
menu_ingame_opt = ('1', '2', '3', '4', '5')

menu_13 = ("*" * 140) + "\n" + (" " * 7) + \
          "   _____  __                            ____                                         ____   __" + \
          "\n" + (" " * 7) + \
          "  / ___/ / /_   ____  _      __        / __ \ ___   ____ ___   ____  _   __ ___     / __ \ / /____ _ __  " \
          "__ ___   _____ _____" + "\n" + (" " * 7) + \
          "  \__ \ / __ \ / __ \| | /| / /______ / /_/ // _ \ / __ `__ \ / __ \| | / // _ \   / /_/ // // __ `// / /" \
          " // _ \ / ___// ___/" + "\n" + (" " * 7) + \
          " ___/ // / / // /_/ /| |/ |/ //_____// _, _//  __// / / / / // /_/ /| |/ //  __/  / ____// // /_/ // /_/ " \
          "//  __// /   (__  )" + "\n" + (" " * 7) + \
          "/____//_/ /_/ \____/ |__/|__/       /_/ |_| \___//_/ /_/ /_/ \____/ |___/ \___/  /_/    /_/ \__,_/ \_" \
          "_, / \___//_/   /____/" + "\n" + (" " * 7) + \
          "                                                                                                  /__" \
          "__/" + "\n\n" + ("*" * 140)

menu_23 = ("*" * 140) + "\n" + (" " * 26) + \
          "   _____        __     __  ___                ____                            __" + "\n" + (" " * 26) + \
          "  / ___/ ___   / /_   /  |/  /____ _ _  __   / __ \ ____   __  __ ____   ____/ /_____" + "\n" + \
          (" " * 26) + \
          "  \__ \ / _ \ / __/  / /|_/ // __ `/| |/_/  / /_/ // __ \ / / / // __ \ / __  // ___/" + "\n" + \
          (" " * 26) + \
          " ___/ //  __// /_   / /  / // /_/ /_>  <   / _, _// /_/ // /_/ // / / // /_/ /(__  )" + "\n" + \
          (" " * 26) + \
          "/____/ \___/ \__/  /_/  /_/ \__,_//_/|_|  /_/ |_| \____/ \__,_//_/ /_/ \__,_//____/" + "\n\n" + ("*" * 140)


menu_21 = ("*" * 140) + "\n" + (" " * 20) + \
          "   _____        __     ______                           ____   __" + "\n" + (" " * 20) + \
          "  / ___/ ___   / /_   / ____/____ _ ____ ___   ___     / __ \ / /____ _ __  __ ___   _____ _____" +\
          "\n" + (" " * 20) + \
          "  \__ \ / _ \ / __/  / / __ / __ `// __ `__ \ / _ \   / /_/ // // __ `// / / // _ \ / ___// ___/" +\
          "\n" + (" " * 20) + \
          " ___/ //  __// /_   / /_/ // /_/ // / / / / //  __/  / ____// // /_/ // /_/ //  __// /   (__  )" +\
          "\n" + (" " * 20) + \
          "/____/ \___/ \__/   \____/ \__,_//_/ /_/ /_/ \___/  /_/    /_/ \__,_/ \__, / \___//_/   /____/" +\
          "\n" + (" " * 20) + \
          "                                                                     /____/" + "\n\n" + ("*" * 140)

Seven_and_half = ("*" * 140) + "\n" + (" " * 37) + \
                 "_____                         ___              __   __  __      ______" + (" " * 33) + "\n" + \
                 (" " * 36) + \
                 "/ ___/___ _   _____  ____     /   |  ____  ____/ /  / / / /___ _/ / __/" + "\n" + (" " * 36) + \
                 "\__ \/ _ \ | / / _ \/ __ \   / /| | / __ \/ __  /  / /_/ / __ `/ / /" + "\n" + (" " * 35) + \
                 "___/ /  __/ |/ /  __/ / / /  / ___ |/ / / / /_/ /  / __  / /_/ / / __/" + "\n" + (" " * 34) + \
                 "/____/\___/|___/\___/_/ /_/  /_/  |_/_/ /_/\__,_/  /_/ /_/\__,_/_/_/" + "\n\n"


game_over = ("*" * 140) + "\n\n" + (" " * 20) + \
          " .d8888b.                                      .d88888b." + "\n" + (" " * 20) + \
          "d88P  Y88b                                    d88P   Y88b" + "\n" + (" " * 20) + \
          "888    888                                    888     888" + "\n" + (" " * 20) + \
          "888         8888b.  88888b.d88b.   .d88b.     888     888 888  888  .d88b.  888d888" + "\n" + (" " * 20) + \
          "888  88888      88b 888  888  88b d8P  Y8b    888     888 888  888 d8P  Y8b 888P " + "\n" + (" " * 20) + \
          "888    888 .d888888 888  888  888 88888888    888     888 Y88  88P 88888888 888" + "\n" + (" " * 20) + \
          "Y88b  d88P 888  888 888  888  888 Y8b.        Y88b. .d88P  Y8bd8P  Y8b.     888" + "\n" + (" " * 20) + \
          "  Y8888P88  Y888888 888  888  888   Y8888       Y88888P     Y88P     Y8888  888" + "\n\n\n" + ("*" * 140)