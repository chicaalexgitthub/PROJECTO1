# Aqui guardamos los datos
letras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N",
          13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K", 22: "E"}

mazo = {"mazo_default": {
    "B01": {"literal ": "As de Bastos", "value": 1, "priority ": 1, "realValue": 1},
    "B02": {"literal ": "Dos de Bastos", "value": 2, "priority ": 1, "realValue": 2},
    "B03": {"literal ": "Tres de Bastos", "value": 3, "priority ": 1, "realValue": 3},
    "B04": {"literal ": "Cuatro de Bastos", "value": 4, "priority ": 1, "realValue": 4},
    "B05": {"literal ": "Cinco de Bastos", "value": 5, "priority ": 1, "realValue": 5},
    "B06": {"literal ": "Seis de Bastos", "value": 6, "priority ": 1, "realValue": 6},
    "B07": {"literal ": "Siete de Bastos", "value": 7, "priority ": 1, "realValue": 7},
    "B08": {"literal ": "Ocho de Bastos", "value": 8, "priority ": 1, "realValue": 0.5},
    "B09": {"literal ": "Nueve de Bastos", "value": 9, "priority ": 1, "realValue": 0.5},
    "B10": {"literal ": "Diez de Bastos", "value": 10, "priority ": 1, "realValue": 0.5},
    "B11": {"literal ": "Once de Bastos", "value": 11, "priority ": 1, "realValue": 0.5},
    "B12": {"literal ": "Doce de Bastos", "value": 12, "priority ": 1, "realValue": 0.5},
    "E01": {"literal ": "As de Espadas", "value": 1, "priority ": 2, "realValue": 1},
    "E02": {"literal ": "Dos de Espadas", "value": 2, "priority ": 2, "realValue": 2},
    "E03": {"literal ": "Tres de Espadas", "value": 3, "priority ": 2, "realValue": 3},
    "E04": {"literal ": "Cuatro de Espadas", "value": 4, "priority ": 2, "realValue": 4},
    "E05": {"literal ": "Cinco de Espadas", "value": 5, "priority ": 2, "realValue": 5},
    "E06": {"literal ": "Seis de Espadas", "value": 6, "priority ": 2, "realValue": 6},
    "E07": {"literal ": "Siete de Espadas", "value": 7, "priority ": 2, "realValue": 7},
    "E08": {"literal ": "Ocho de Espadas", "value": 8, "priority ": 2, "realValue": 0.5},
    "E09": {"literal ": "Nueve de Espadas", "value": 9, "priority ": 2, "realValue": 0.5},
    "E10": {"literal ": "Diez de Espadas", "value": 10, "priority ": 2, "realValue": 0.5},
    "E11": {"literal ": "Once de Espadas", "value": 11, "priority ": 2, "realValue": 0.5},
    "E12": {"literal ": "Doce de Espadas", "value": 12, "priority ": 2, "realValue": 0.5},
    "C01": {"literal ": "As de Copas", "value": 1, "priority ": 3, "realValue": 1},
    "C02": {"literal ": "Dos de Copas", "value": 2, "priority ": 3, "realValue": 2},
    "C03": {"literal ": "Tres de Copas", "value": 3, "priority ": 3, "realValue": 3},
    "C04": {"literal ": "Cuatro de Copas", "value": 4, "priority ": 3, "realValue": 4},
    "C05": {"literal ": "Cinco de Copas", "value": 5, "priority ": 3, "realValue": 5},
    "C06": {"literal ": "Seis de Copas", "value": 6, "priority ": 3, "realValue": 6},
    "C07": {"literal ": "Siete de Copas", "value": 7, "priority ": 3, "realValue": 7},
    "C08": {"literal ": "Ocho de Copas", "value": 8, "priority ": 3, "realValue": 0.5},
    "C09": {"literal ": "Nueve de Copas", "value": 9, "priority ": 3, "realValue": 0.5},
    "C10": {"literal ": "Diez de Copas", "value": 10, "priority ": 3, "realValue": 0.5},
    "C11": {"literal ": "Once de Copas", "value": 11, "priority ": 3, "realValue": 0.5},
    "C12": {"literal ": "Doce de Copas", "value": 12, "priority ": 3, "realValue": 0.5},
    "O01": {"literal ": "As de Oros", "value": 1, "priority ": 4, "realValue": 1},
    "O02": {"literal ": "Dos de Oros", "value": 2, "priority ": 4, "realValue": 2},
    "O03": {"literal ": "Tres de Oros", "value": 3, "priority ": 4, "realValue": 3},
    "O04": {"literal ": "Cuatro de Oros", "value": 4, "priority ": 4, "realValue": 4},
    "O05": {"literal ": "Cinco de Oros", "value": 5, "priority ": 4, "realValue": 5},
    "O06": {"literal ": "Seis de Oros", "value": 6, "priority ": 4, "realValue": 6},
    "O07": {"literal ": "Siete de Oros", "value": 7, "priority ": 4, "realValue": 7},
    "O08": {"literal ": "Ocho de Oros", "value": 8, "priority ": 4, "realValue": 0.5},
    "O09": {"literal ": "Nueve de Oros", "value": 9, "priority ": 4, "realValue": 0.5},
    "O10": {"literal ": "Diez de Oros", "value": 10, "priority ": 4, "realValue": 0.5},
    "O11": {"literal ": "Once de Oros", "value": 11, "priority ": 4, "realValue": 0.5},
    "O12": {"literal ": "Doce de Oros", "value": 12, "priority ": 4, "realValue": 0.5}, }, "mazo_1": {
    "B01": {"literal ": "As de Bastos", "value": 1, "priority ": 1, "realValue": 1},
    "B02": {"literal ": "Dos de Bastos", "value": 2, "priority ": 1, "realValue": 2},
    "B03": {"literal ": "Tres de Bastos", "value": 3, "priority ": 1, "realValue": 3},
    "B04": {"literal ": "Cuatro de Bastos", "value": 4, "priority ": 1, "realValue": 4},
    "B05": {"literal ": "Cinco de Bastos", "value": 5, "priority ": 1, "realValue": 5},
    "B06": {"literal ": "Seis de Bastos", "value": 6, "priority ": 1, "realValue": 6},
    "B07": {"literal ": "Siete de Bastos", "value": 7, "priority ": 1, "realValue": 7},
    "B10": {"literal ": "Diez de Bastos", "value": 10, "priority ": 1, "realValue": 0.5},
    "B11": {"literal ": "Once de Bastos", "value": 11, "priority ": 1, "realValue": 0.5},
    "B12": {"literal ": "Doce de Bastos", "value": 12, "priority ": 1, "realValue": 0.5},
    "E01": {"literal ": "As de Espadas", "value": 1, "priority ": 2, "realValue": 1},
    "E02": {"literal ": "Dos de Espadas", "value": 2, "priority ": 2, "realValue": 2},
    "E03": {"literal ": "Tres de Espadas", "value": 3, "priority ": 2, "realValue": 3},
    "E04": {"literal ": "Cuatro de Espadas", "value": 4, "priority ": 2, "realValue": 4},
    "E05": {"literal ": "Cinco de Espadas", "value": 5, "priority ": 2, "realValue": 5},
    "E06": {"literal ": "Seis de Espadas", "value": 6, "priority ": 2, "realValue": 6},
    "E07": {"literal ": "Siete de Espadas", "value": 7, "priority ": 2, "realValue": 7},
    "E10": {"literal ": "Diez de Espadas", "value": 10, "priority ": 2, "realValue": 0.5},
    "E11": {"literal ": "Once de Espadas", "value": 11, "priority ": 2, "realValue": 0.5},
    "E12": {"literal ": "Doce de Espadas", "value": 12, "priority ": 2, "realValue": 0.5},
    "C01": {"literal ": "As de Copas", "value": 1, "priority ": 3, "realValue": 1},
    "C02": {"literal ": "Dos de Copas", "value": 2, "priority ": 3, "realValue": 2},
    "C03": {"literal ": "Tres de Copas", "value": 3, "priority ": 3, "realValue": 3},
    "C04": {"literal ": "Cuatro de Copas", "value": 4, "priority ": 3, "realValue": 4},
    "C05": {"literal ": "Cinco de Copas", "value": 5, "priority ": 3, "realValue": 5},
    "C06": {"literal ": "Seis de Copas", "value": 6, "priority ": 3, "realValue": 6},
    "C07": {"literal ": "Siete de Copas", "value": 7, "priority ": 3, "realValue": 7},
    "C10": {"literal ": "Diez de Copas", "value": 10, "priority ": 3, "realValue": 0.5},
    "C11": {"literal ": "Once de Copas", "value": 11, "priority ": 3, "realValue": 0.5},
    "C12": {"literal ": "Doce de Copas", "value": 12, "priority ": 3, "realValue": 0.5},
    "O01": {"literal ": "As de Oros", "value": 1, "priority ": 4, "realValue": 1},
    "O02": {"literal ": "Dos de Oros", "value": 2, "priority ": 4, "realValue": 2},
    "O03": {"literal ": "Tres de Oros", "value": 3, "priority ": 4, "realValue": 3},
    "O04": {"literal ": "Cuatro de Oros", "value": 4, "priority ": 4, "realValue": 4},
    "O05": {"literal ": "Cinco de Oros", "value": 5, "priority ": 4, "realValue": 5},
    "O06": {"literal ": "Seis de Oros", "value": 6, "priority ": 4, "realValue": 6},
    "O07": {"literal ": "Siete de Oros", "value": 7, "priority ": 4, "realValue": 7},
    "O10": {"literal ": "Diez de Oros", "value": 10, "priority ": 4, "realValue": 0.5},
    "O11": {"literal ": "Once de Oros", "value": 11, "priority ": 4, "realValue": 0.5},
    "O12": {"literal ": "Doce de Oros", "value": 12, "priority ": 4, "realValue": 0.5}, }}

players = {"11115555A":
               {"name": "Mario", "human": True, "bank": False, "initialCard": "", "priority": 0,
                "type": 40, "bet": 4, "points": 0, "cards ": [], "roundPoints": 0},
           "22225555A":
               {"name": "Pedro", "human": True, "bank": False, "initialCard": "", "priority": 0,
                "type": 40, "bet": 4, "points": 0, "cards ": [], "roundPoints ": 0}}

cardgame = {'cardgame_id': 0, 'players': 0, 'start_hour': 0,
            'rounds': 0, 'end_hour': 0}

player_game = {"id_game": {"id_player_1": {"initial_card_id": 0, "starting_points": 0, "ending_points": 0}}}

player_game_round = {"round": {"id_player_1": {"is_bank": 0, "bet_points": 0, "cards_value": 0,
                                               "ending_round_points": 0}}}

context_game = {"game": [], "mazo": [], "round": []}

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
        "".ljust(39) + "  Y888b.    .d88b. 888888 888888 888 88888b.   .d88b.  .d8888b\n" + \
        "".ljust(42) + " Y88b. d8P  Y8b 888    888    888 888  88b d88P 88b 88K\n" + \
        "".ljust(43) + "  888 88888888 888    888    888    888 888  888 888  Y8888b.\n" + \
        "".ljust(38) + "Y88b  d88P Y8b.     Y88b.  Y88b.  888 888  888 Y88b 888      X88\n" + \
        "".ljust(39) + " Y8888P    Y8888    Y888   Y888 888 888   888   Y88888  88888P\n" + \
        "".ljust(30) + "888\n" + \
        "".ljust(30) + "Y8b d88P\n"              + \
        "".ljust(30) + "Y88P\n" + ("*" * 140) + "\n\n" + "1)Set Game Players\n".rjust(73) + \
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
