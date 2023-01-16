from mysql.connector import *
import os
import random
from Paquetes import datos as d
#Conectamos con la base de datos
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


def detector_mazo(mazo):
    # Se utiliza esta pequeña funcion para determinar con que mazo estamos trabajando
    if mazo[0] in d.mazo["mazo_default"]:
        return "mazo_default"
    elif mazo[0] in d.mazo["mazo_1"]:
        return "mazo_1"


def set_game_priority(mazo):
    # barajamos el mazo
    mazo = barajar_mazo(mazo)
    # determinamos que mazo estamos usando
    mazo_opt = detector_mazo(mazo)
    # Le asignamos a cada jugador una carta del mazo
    for i in d.context_game["game"]:
        d.players[i]["initialCard"] = mazo[random.randint(0, len(mazo))]
    # Ordenamos la lista de jugadores segun la prioridad de sus cartas
    for i in d.context_game["game"]:
        for j in d.context_game["game"]:
            # Primero se mira si la prioridad de la carta es la misma, en ese caso comparamos el valor de las cartas
            if d.mazo[mazo_opt][d.players[i]["initialCard"]]["priority "] == \
                    d.mazo[mazo_opt][d.players[j]["initialCard"]]["priority "]:
                if d.mazo[mazo_opt][d.players[i]["initialCard"]]["value"] < \
                        d.mazo[mazo_opt][d.players[j]["initialCard"]]["value"]:
                    d.context_game["game"][d.context_game["game"].index(i)], \
                    d.context_game["game"][d.context_game["game"].index(j)] = \
                        d.context_game["game"][d.context_game["game"].index(j)], \
                        d.context_game["game"][d.context_game["game"].index(i)]
            # Si la prioridad de la carta no es la misma, comparamos la prioridad
            else:
                if d.mazo[mazo_opt][d.players[i]["initialCard"]]["priority "] < \
                        d.mazo[mazo_opt][d.players[j]["initialCard"]]["priority "]:
                    d.context_game["game"][d.context_game["game"].index(i)], \
                    d.context_game["game"][d.context_game["game"].index(j)] = \
                        d.context_game["game"][d.context_game["game"].index(j)], \
                        d.context_game["game"][d.context_game["game"].index(i)]
    # Le asignamos a cada jugador su prioridad basada en su posicion en la lista de jugadores
    for i in range(0, len(d.context_game["game"])):
        d.players[d.context_game["game"][i]]["priority"] = len(d.context_game["game"] - 1)
        # El que tiene mas prioridad (primero de la lista) es la banca
        if i == 0:
            d.players[d.context_game["game"][i]]["bank"] = True
        else:
            d.players[d.context_game["game"][i]]["bank"] = False
    # devolvemos la variable
    return mazo


def reset_points():
    # Establecemos en 20 los puntos de todos los jugadores
    for i in d.context_game["game"]:
        d.players[i]["points"] = 20


def check_minimum_2_player_with_points():
    # Establecemos un contador
    count = 0
    # Se recorre la lista de jugadores de la partida actual
    for i in d.context_game["game"]:
        # En caso de que los puntos de un jugador sean mayores a 0, se suma 1 al contador
        if d.players[i]["points"] > 0:
            count += 1
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
        profile = 1
    if profile == 'Bold':
        profile = 1
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
    if len(bots) > len(humans):
        x = bots
    else:
        x = humans
    for i in range(0, len(x)):
        if i < len(bots):
            print(d.players[bots[i]], end="  ")
        print(d.players[humans[i]])


# FUNCION REQUERIDA: EN FUNCION DE LA PERSONALIDAD DEL JUGADOR HACER UNA APUESTA U OTRA (personalidad, puntos_disponibles)
def bet_on_risk(risk, points):
    percentage = random.randint(1, 100)
    print(percentage)
    if risk == 30:
        points = points * 0.3
    elif risk == 40:
        points = points * 0.5
    elif risk == 50:
        points = points * 1

    if int(points*(percentage/100)) < 1:
        return 1
    else:
        return int(points*(percentage/100))


# Función que elimina un jugador de la BBDD
def delBBDDPlayer(nif):
    query = "DELETE FROM player where player_id = %s"
    cursorObject.execute(query,(nif,))
    database.commit()


# FUNCION REQUERIDA: Eliminar todos los ROUNDPOINT de los jugadores que esten en partida, en el diccionario context_game de
# dades, dentro de game, estan los id de los jugadores de la partida
# la variable player_list es una lista
def reset_roundpoint (player_list):
    for user in player_list:
        d.players[user]["roundPoints"] = 0


# Función que devuelve un id no existente en la tabla cardgame.
def getGameId():
    query = "SELECT cardgame_id from cardgame"
    cursorObject.execute(query)
    all_id = cursorObject.fetchall()

    id_list = []
    for i in all_id:
        id_list.append(i[0])

    while True:
        new_id = random.randint(1, 999)
        if new_id not in id_list:
            return new_id


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

