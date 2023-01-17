from mysql.connector import *
import os
import random
from Paquetes import datos as d

# Conectamos con la base de datos
database = connect(user="gameadmin", password="sieteymedio123$", host="sevenandhalf.mysql.database.azure.com",
                   database="seven_half")
cursorObject = database.cursor(buffered=True)


# Aqui guardamos las funciones.


def menu(menu_, options, exceptions=""):
    os.system("clear")
    print(menu_)
    opt = input("Option: ".rjust(62))
    try:
        if not opt.isdigit():
            if not opt in exceptions:
                raise TypeError(("=" * 61) + "Invalid Option" + ("=" * 66))
            elif opt.isspace() or opt == "":
                raise TypeError(("=" * 61) + "Invalid Option" + ("=" * 66))
        if opt not in options:
            if opt not in exceptions:
                raise ValueError(("=" * 61) + "Invalid Option" + ("=" * 66))
        return opt
    except TypeError as error:
        print("\n", error)
        input("Press enter to continue".rjust(79))
        return menu(menu_, options, exceptions)
    except ValueError as error:
        print("\n", error)
        input("Press enter to continue".rjust(79))
        return menu(menu_, options, exceptions)


def barajar_mazo(mazo):
    # Se recorre cada posicion del mazo asignandole una nueva posicion a su valor,
    # y intercambiando los valores de ambas posiciones
    for i in range(0, len(mazo) - 1):
        new_pos = random.randint(0, len(mazo) - 1)
        mazo[i], mazo[new_pos] = mazo[new_pos], mazo[i]
    return mazo


def set_game_priority(mazo):
    given_cards = []
    # Le asignamos a cada jugador una carta del mazo
    for i in d.context_game["game"]:
        d.players[i]["initialCard"] = mazo[random.randint(0, len(mazo) - 1)]
        given_cards.append(d.players[i]["initialCard"])
    # Ordenamos la lista de jugadores segun la prioridad de sus cartas
    for i in d.context_game["game"]:
        for j in d.context_game["game"]:
            # Primero se mira si la prioridad de la carta es la misma, en ese caso comparamos el valor de las cartas
            if d.mazo[d.players[i]["initialCard"]]["priority "] == \
                    d.mazo[d.players[j]["initialCard"]]["priority "]:
                if d.mazo[d.players[i]["initialCard"]]["value"] > \
                        d.mazo[d.players[j]["initialCard"]]["value"]:
                    d.context_game["game"][d.context_game["game"].index(i)], \
                    d.context_game["game"][d.context_game["game"].index(j)] = \
                        d.context_game["game"][d.context_game["game"].index(j)], \
                        d.context_game["game"][d.context_game["game"].index(i)]
            # Si la prioridad de la carta no es la misma, comparamos la prioridad
            else:
                if d.mazo[d.players[i]["initialCard"]]["priority "] > \
                        d.mazo[d.players[j]["initialCard"]]["priority "]:
                    d.context_game["game"][d.context_game["game"].index(i)], \
                    d.context_game["game"][d.context_game["game"].index(j)] = \
                        d.context_game["game"][d.context_game["game"].index(j)], \
                        d.context_game["game"][d.context_game["game"].index(i)]
    establish_banca()
    bank = None
    for x in d.context_game["game"]:
        if d.players[x]["bank"] is True:
            bank = x
    for i in range(0, len(d.context_game)):
        d.players[d.context_game["game"][i]]["priority"] = i + 1
    # devolvemos la variable
    d.context_game["game"] = invert_list(d.context_game["game"])
    return given_cards


def establish_banca():
    for i in range(0, len(d.context_game["game"])):
        d.players[d.context_game["game"][i]]["priority"] = len(d.context_game["game"]) - 1
        # El que tiene mas prioridad (primero de la lista) es la banca
        if i == 0:
            d.players[d.context_game["game"][i]]["bank"] = True
        else:
            d.players[d.context_game["game"][i]]["bank"] = False
    return


def reset_points():
    # Establecemos en 20 los puntos de todos los jugadores
    for i in d.context_game["game"]:
        d.players[i]["points"] = 20


def reset_roundPoints():
    for i in d.context_game["game"]:
        d.players[i]["roundPoints"] = 0


def check_minimum_2_player_with_points():
    # Establecemos un contador
    count = 0
    eliminated = []
    # Se recorre la lista de jugadores de la partida actual
    for i in d.context_game["game"]:
        # En caso de que los puntos de un jugador sean mayores a 0, se suma 1 al contador
        if d.players[i]["points"] > 0:
            count += 1
        else:
            eliminated.append(i)
    for x in eliminated:
        del d.context_game["game"][d.context_game["game"].index(x)]
    # En caso de que el contador sea mayor de 1 (minimo 2), se devuelve TRUE, si no se devuelve FALSE
    if count > 1:
        return True
    else:
        return False


def check_conditions():
    try:
        if len(d.context_game["game"]) < 2:
            raise ValueError("Set the players that compose the game first".rjust(97))
        if len(d.mazo) == 0:
            raise ValueError("Set the deck of cards first".rjust(82))
        return
    except ValueError as error:
        print(error)
        input("Press enter to continue".rjust(77))


def create_human_player_name():
    try:
        os.system("clear")
        print(d.players_banner)
        name = input("Name: ".rjust(45))
        if not name.isspace() or not name == "":
            if not name.isalnum() and not name.isalpha() and not name.isdigit():
                raise TypeError("Incorrect name, please, enter a name not empty with only letters.".rjust(104))
            os.system("clear")
            print(d.players_banner)
        print("Name:        ".rjust(52), name)
        return name
    except TypeError as error:
        print(error)
        input("Enter to continue".rjust(56))
        return create_human_player_name()


def create_human_player_nif(name):
    nif = input("NIF: ".rjust(44))
    try:
        if not len(nif) == 9:
            raise ValueError("Invalid NIF length")
        if not nif[0:7].isdigit() or not nif[8].isalpha():
            raise TypeError("Invalid NIF format")
        if not nif[8] == d.letras[int(nif[0:8]) % 23]:
            raise ValueError("Invalid NIF letter")
        os.system("clear")
        print(d.players_banner)
        print("Name:        ".rjust(52), name)
        print("NIF:         ".rjust(52), nif)
        return nif
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)
    input("Enter to continue")
    os.system("clear")
    print(d.players_banner)
    print("Name:        ".rjust(52), name)
    return create_human_player_nif(name)


def create_human_player_profile(name, nif):
    print((" " * 38), "Select your profile:\n",
          (" " * 37), "1)Cautious\n",
          (" " * 37), "2)Moderated\n",
          (" " * 37), "3)Bold")
    profile = input("Option: ".rjust(47))
    try:
        if not profile in ('1', '2', '3'):
            raise ValueError("Invalid option")
        if profile == '1':
            profile = 'Cautious'
        elif profile == '2':
            profile = 'Moderated'
        elif profile == '3':
            profile = 'Bold'
        os.system("clear")
        print(d.players_banner, "\n", "Name:        ".rjust(51), name, "\n", "NIF:         ".rjust(51), nif,
              "\n" + "Profile:     ".rjust(52), profile)
        return profile
    except ValueError as error:
        print((' ' * 38), error)
        input("Enter to continue".rjust(56))
        os.system("clear")
        print(d.players_banner, "\n", "Name:        ".rjust(51), name, "\n", "NIF:         ".rjust(51), nif)
        return create_human_player_profile(name, nif)


def create_human_player():
    name = create_human_player_name()
    nif = create_human_player_nif(name)
    profile = create_human_player_profile(name, nif)
    save = create_human_player_check(name, nif, profile)
    if profile == 'Cautious':
        profile = 1
    if profile == 'Moderated':
        profile = 2
    if profile == 'Bold':
        profile = 3
    if save:
        d.players[nif] = {"name": name, "human": True, "bank": False, "initialCard": "", "priority": 0,
                          "type": 40, "bet": 4, "points": 0, "cards ": [], "roundPoints": 0}


def create_human_player_check(name, nif, profile):
    opt = input("Is okay? Y/n: ".rjust(53))
    try:
        if opt.lower() == 'y':
            return True
        elif opt.lower() == 'n':
            return False
        else:
            raise ValueError(("=" * 61) + "Invalid Option" + ("=" * 66) + "\n")
    except ValueError as error:
        print(error)
        input("Press enter to continue".rjust(79))
    os.system("clear")
    print(d.players_banner, "\n", "Name:        ".rjust(51), name, "\n", "NIF:         ".rjust(51), nif,
          "\n" + "Profile:     ".rjust(52), profile)
    return create_human_player_check(name, nif, profile)


def insert_players():
    query = ("SELECT player_id FROM PLAYER")
    cursorObject.execute(query)
    database.commit()
    result_raw = cursorObject.fetchall()
    result = []
    for x in result_raw:
        result.append(x[0])
    players = d.players.keys()
    for x in players:
        if not x in result:
            query = ("INSERT INTO player VALUES (%s, %s, %s, %s)")
            values = [(x, d.players[x]["name"], d.players[x]["type"], d.players[x]["human"])]
            cursorObject.executemany(query, values)
            database.commit()
    database.close()


def get_deck(deck):
    query = ("SELECT * FROM card WHERE deck_id = {}".format(deck))
    cursorObject.execute(query)
    database.commit()
    result_raw = cursorObject.fetchall()
    result = []
    for x in result_raw:
        d.mazo[x[0]] = {"literal": x[1], "value": x[5], "priority": x[4], "real value": float(x[2])}


def random_nif():
    nif = ""
    for x in range(0, 8):
        nif += str(random.randint(0, 9))
    letter = d.letras[int(nif) % 23]
    nif += letter
    if not nif in d.players:
        return nif
    else:
        return random_nif()


def create_boot():
    name = create_human_player_name()
    nif = random_nif()
    profile = create_human_player_profile(name, nif)
    save = create_human_player_check(name, nif, profile)
    if save:
        d.players[nif] = {"name": name, "human": False, "bank": False, "initialCard": "", "priority": 0,
                          "type": 40, "bet": 4, "points": 0, "cards ": [], "roundPoints": 0}


def show_players():
    print("Select players".center(140, '*'))
    print("Boot Player".center(68) + "||" + "Human Players".center(68))
    print('-' * 140)
    print("ID".ljust(21) + "Name".ljust(24) + "Type".ljust(23) + "||", end="  ")
    print("ID".ljust(21) + "Name".ljust(24) + "Type")
    print('*' * 140)
    bots = []
    humans = []
    for x in d.players:
        if d.players[x]["human"] is False:
            bots.append(x)
        else:
            humans.append(x)
    bots = []
    humans = []
    order = []
    for x in d.players:
        if d.players[x]["human"] is False:
            bots.append(x)
        else:
            humans.append(x)


def bet_on_risk(nif):
    if d.players[nif]["type"] == 30:
        d.players[nif]["bet"] = d.players[nif]["points"] // 4
    elif d.players[nif]["type"] == 40:
        d.players[nif]["bet"] = d.players[nif]["points"] // 2
    elif d.players[nif]["type"] == 60:
        d.players[nif]["bet"] = d.players[nif]["points"] * 1


def invert_list(lista):
    lista_invertida = []
    for i in range(len(lista)):
        lista_invertida.append(lista[-1])
        lista = lista[:-1]
    return lista_invertida


def setMaxRounds():
    try:
        maxRounds = input("Max Rounds: ")
        if maxRounds.isdigit() and int(maxRounds) in range(1, 21):
            d.context_game.update({"maxRounds": maxRounds})
        elif maxRounds.isdigit() and int(maxRounds) < 1:
            raise ValueError("Please, enter only positive numbers")
        elif maxRounds.isdigit() and int(maxRounds) > 20:
            raise ValueError("Max Rounds Has To Be Between 0 and 20")
        else:
            raise ValueError("Please, enter only numbers")
    except ValueError as error:
        print(error)
        setMaxRounds()

def check_valid_bet(total_points):
    try:
        bet = input("Set the new Bet: ")
        if not bet.isdigit():
            raise TypeError("Please, introduce only numbers")
        elif int(bet) > total_points or int(bet) <= 0:
            raise ValueError("The New Bet has to be a number between 1 and " + str(total_points))
        else:
            return int(bet)

    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

    return check_valid_bet(total_points)


# Funcion para saber el porcetage de sacar mas de 7.5
def moreThan7_half(current_points, available_cards):
    total = len(available_cards)
    losing_cards = 0
    for card in available_cards:
        if (d.mazo[card]["realValue"] + current_points) > 7.5:
            losing_cards += 1

    return losing_cards/total
