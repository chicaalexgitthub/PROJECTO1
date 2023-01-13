# Aqui guardamos los datos
letras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N",
          13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K", 22: "E"}

mazo = {}

players = {"11115555A":
               {"name": "Mario", "human": True, "bank": False, "initialCard": "", "priority": 0,
                "type": 40, "bet": 4, "points": 0, "cards ": [], "roundPoints": 0},
           "22225555A":
               {"name": "Pedro", "human": True, "bank": False, "initialCard": "", "priority": 0,
                "type": 40, "bet": 4, "points": 0, "cards ": [], "roundPoints": 0},
           "21115555A":
               {"name": "Mario", "human": False, "bank": False, "initialCard": "", "priority": 0,
                "type": 40, "bet": 4, "points": 0, "cards ": [], "roundPoints": 0}
           }

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
          "".ljust(39) + "Y88b.              888    888\n" + \
          "".ljust(39) + "  Y888b.    .d88b. 888888 888888 888 88888b.   .d88b.  .d8888b\n" + \
          "".ljust(42) + " Y88b. d8P  Y8b 888    888    888 888  88b d88P 88b 88K\n" + \
          "".ljust(43) + "  888 88888888 888    888    888    888 888  888 888  Y8888b.\n" + \
          "".ljust(38) + "Y88b  d88P Y8b.     Y88b.  Y88b.  888 888  888 Y88b 888      X88\n" + \
          "".ljust(39) + " Y8888P    Y8888    Y888   Y888 888 888   888   Y88888  88888P\n" + \
          "".ljust(30) + "888\n" + \
          "".ljust(30) + "Y8b d88P\n" + \
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

menu_022 = ("*" * 140) + "\n" + ("*" * 140) + "\n" + "1) ESP - ESP\n" + \
           "2) POK - POK\n" + "0) Go back"
menu_022_opt = ('1', '2', '0')
