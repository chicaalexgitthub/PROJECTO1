from mysql.connector import *
import os
import random
from Paquetes.datos import *
from math import *

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


def set_game_priority(deck):
    given_cards = []
    # Le asignamos a cada jugador una carta del mazo
    for i in context_game["game"]:
        players[i]["initialCard"] = deck[random.randint(0, len(deck) - 1)]
        given_cards.append(players[i]["initialCard"])
    # Ordenamos la lista de jugadores segun la prioridad de sus cartas
    for i in context_game["game"]:
        for j in context_game["game"]:
            # Primero se mira si la prioridad de la carta es la misma, en ese caso comparamos el valor de las cartas
            if mazo[players[i]["initialCard"]]["priority"] == \
                    mazo[players[j]["initialCard"]]["priority"]:
                if mazo[players[i]["initialCard"]]["value"] > \
                        mazo[players[j]["initialCard"]]["value"]:
                    context_game["game"][context_game["game"].index(i)], \
                    context_game["game"][context_game["game"].index(j)] = \
                        context_game["game"][context_game["game"].index(j)], \
                        context_game["game"][context_game["game"].index(i)]
            # Si la prioridad de la carta no es la misma, comparamos la prioridad
            else:
                if mazo[players[i]["initialCard"]]["priority"] > \
                        mazo[players[j]["initialCard"]]["priority"]:
                    context_game["game"][context_game["game"].index(i)], \
                    context_game["game"][context_game["game"].index(j)] = \
                        context_game["game"][context_game["game"].index(j)], \
                        context_game["game"][context_game["game"].index(i)]
    establish_bank()
    bank = None
    for x in context_game["game"]:
        if players[x]["bank"] is True:
            bank = x
    for i in range(0, len(context_game["game"])):
        players[context_game["game"][i]]["priority"] = len(context_game["game"][i:])
        print(players[context_game["game"][i]]["priority"])
    # devolvemos la variable
    context_game["game"] = invert_list(context_game["game"])
    return given_cards


def establish_bank():
    for i in range(0, len(context_game["game"])):
        players[context_game["game"][i]]["priority"] = len(context_game["game"]) - 1
        # El que tiene mas prioridad (primero de la lista) es la banca
        if i == 0:
            players[context_game["game"][i]]["bank"] = True
        else:
            players[context_game["game"][i]]["bank"] = False
    return


def reset_points():
    # Establecemos en 20 los puntos de todos los jugadores
    for i in context_game["game"]:
        players[i]["points"] = 20


def reset_roundPoints():
    for i in context_game["game"]:
        players[i]["roundPoints"] = 0


def check_minimum_2_player_with_points():
    # Establecemos un contador
    count = 0
    eliminated = []
    # Se recorre la lista de jugadores de la partida actual
    for i in context_game["game"]:
        # En caso de que los puntos de un jugador sean mayores a 0, se suma 1 al contador
        if players[i]["points"] > 0:
            count += 1
        else:
            eliminated.append(i)
    for x in eliminated:
        del context_game["game"][context_game["game"].index(x)]
    # En caso de que el contador sea mayor de 1 (minimo 2), se devuelve TRUE, si no se devuelve FALSE
    if count > 1:
        return True
    else:
        return False


def check_conditions():
    try:
        if len(context_game["game"]) < 2:
            raise ValueError("Set the players that compose the game first".rjust(97))
        if len(mazo) == 0:
            get_deck(1)
        return True
    except ValueError as error:
        print(error)
        input("Press enter to continue".rjust(77))
        return False


def create_human_player_name():
    try:
        os.system("clear")
        print(players_banner)
        name = input("Name: ".rjust(45))
        if not name.isspace() or not name == "":
            if not name.isalnum() and not name.isalpha() and not name.isdigit():
                raise TypeError("Incorrect name, please, enter a name not empty with only letters.".rjust(104))
            os.system("clear")
            print(players_banner)
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
        if not nif[8] == letras[int(nif[0:8]) % 23]:
            raise ValueError("Invalid NIF letter")
        os.system("clear")
        print(players_banner)
        print("Name:        ".rjust(52), name)
        print("NIF:         ".rjust(52), nif)
        return nif
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)
    input("Enter to continue")
    os.system("clear")
    print(players_banner)
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
        print(players_banner, "\n", "Name:        ".rjust(51), name, "\n", "NIF:         ".rjust(51), nif,
              "\n" + "Profile:     ".rjust(52), profile)
        return profile
    except ValueError as error:
        print((' ' * 38), error)
        input("Enter to continue".rjust(56))
        os.system("clear")
        print(players_banner, "\n", "Name:        ".rjust(51), name, "\n", "NIF:         ".rjust(51), nif)
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
        players[nif] = {"name": name, "human": True, "bank": False, "initialCard": "", "priority": 0,
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
    print(players_banner, "\n", "Name:        ".rjust(51), name, "\n", "NIF:         ".rjust(51), nif,
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
    player_list = players.keys()
    for x in player_list:
        if not x in result:
            query = ("INSERT INTO player VALUES (%s, %s, %s, %s)")
            values = [(x, players[x]["name"], players[x]["type"], players[x]["human"])]
            cursorObject.executemany(query, values)
            database.commit()


def get_deck(deck):
    query = ("SELECT * FROM card WHERE deck_id = {}".format(deck))
    cursorObject.execute(query)
    database.commit()
    result_raw = cursorObject.fetchall()
    result = []
    for x in result_raw:
        mazo[x[0]] = {"literal": x[1], "value": x[5], "priority": x[4], "realValue": float(x[2])}


def random_nif():
    nif = ""
    for x in range(0, 8):
        nif += str(random.randint(0, 9))
    letter = letras[int(nif) % 23]
    nif += letter
    if not nif in players:
        return nif
    else:
        return random_nif()


def create_boot():
    name = create_human_player_name()
    nif = random_nif()
    profile = create_human_player_profile(name, nif)
    if profile == 'Cautious':
        profile = 30
    elif profile == 'Moderated':
        profile = 40
    elif profile == 'Bold':
        profile = 60
    save = create_human_player_check(name, nif, profile)
    if save:
        players[nif] = {"name": name, "human": False, "bank": False, "initialCard": "", "priority": 0,
                          "type": profile, "bet": 4, "points": 0, "cards ": [], "roundPoints": 0}


def show_players():
    os.system("clear")
    print(menu_13)
    print("Select players".center(140, '*'))
    print("Boot Player".center(68) + "||" + "Human Players".center(68))
    print('-' * 140)
    print("ID".ljust(21) + "Name".ljust(24) + "Type".ljust(23) + "||", end="  ")
    print("ID".ljust(21) + "Name".ljust(24) + "Type")
    print('*' * 140)
    bots = []
    humans = []
    for x in players:
        if players[x]["human"] is False:
            bots.append(x)
        else:
            humans.append(x)
    while len(humans) > 0 or len(bots) > 0:
        if len(bots) > 0:
            print(bots[0].ljust(20), players[bots[0]]["name"].ljust(24), end="")
            if players[bots[0]]["type"] == 30:
                print("Cautious".ljust(23), end="||".ljust(4))
            elif players[bots[0]]["type"] == 40:
                print("Moderate".ljust(23), end="||".ljust(4))
            elif players[bots[0]]["type"] == 60:
                print("Bold".ljust(23), end="||".ljust(4))
            del bots[0]
        else:
            print("".ljust(68), end="||".ljust(4))
        if len(humans) > 0:
            print(humans[0].ljust(20), players[humans[0]]["name"].ljust(24), end="")
            if players[humans[0]]["type"] == 30:
                print("Cautious".ljust(23).ljust(8))
            elif players[humans[0]]["type"] == 40:
                print("Moderate".ljust(23).ljust(8))
            elif players[humans[0]]["type"] == 60:
                print("Bold".ljust(23).ljust(8))
            del humans[0]
        else:
            print()
    print("\n\n" + ("*" * 140))
    opt = input("\n\n".ljust(50) + "Option (   -id to remove player, -1 to exit): ")
    if len(opt) > 0:
        if opt[0] == '-' and len(opt) == 10:
            if opt[1:] in players:
                delete_players[opt[1:]] = opt[1:]
                del players[opt[1:]]
                input("Press enter to continue".rjust(71))
                show_players()
        elif opt == '-1':
            print()
        else:
            print(("=" * 66) + "Invalid Option" + ("=" * 66))
            input("Press enter to continue".rjust(71))
            show_players()

    else:
        print(("=" * 66) + "Invalid Option" + ("=" * 66))
        input("Press enter to continue".rjust(71))
        show_players()




def bet_on_risk(nif):
    if players[nif]["type"] == 30:
        players[nif]["bet"] = players[nif]["points"] // 4
    elif players[nif]["type"] == 40:
        players[nif]["bet"] = players[nif]["points"] // 2
    elif players[nif]["type"] == 60:
        players[nif]["bet"] = players[nif]["points"] * 1


def invert_list(lista):
    lista_invertida = []
    for i in range(len(lista)):
        lista_invertida.append(lista[-1])
        lista = lista[:-1]
    return lista_invertida


def setMaxRounds():
    try:
        os.system("clear")
        print(menu_23, "\n\n")
        maxRounds = input("Max Rounds: ".rjust(60))
        if maxRounds.isdigit() and int(maxRounds) in range(1, 21):
            return int(maxRounds)
        elif maxRounds.isdigit() and int(maxRounds) < 1:
            raise ValueError("Please, enter only positive numbers")
        elif maxRounds.isdigit() and int(maxRounds) > 20:
            raise ValueError("Max Rounds Has To Be Between 0 and 20")
        else:
            raise ValueError("Please, enter only numbers")
    except ValueError as error:
        print("".ljust(47), error)
        input("Enter to continue".rjust(65))
        return setMaxRounds()

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
        if (mazo[card]["realValue"] + current_points) > 7.5:
            losing_cards += 1

    return losing_cards/total * 100

def turn(deck, round):
    reset_roundPoints()
    given_cards = []
    # Se realizan las apuestas de cada jugador
    # Recorremos la lista de jugadores ordenada por prioridad ascendente
    opt = 'e'
    reset_cards()
    bank = context_game["game"][len(context_game["game"]) - 1]
    for x in context_game["game"]:
        bet_on_risk(x)
        deck = barajar_mazo(deck)
        if players[x]["human"] is False:
            deck, given_cards = card_phase(deck, given_cards, x)
        else:
            head = Seven_and_half + (" Round " + str(round) + ", " + players[x]["name"] + "'s turn ").center(140, "*")
            head += menu_ingame + "\n"
            opt = menu(head, menu_ingame_opt)
            while not opt == '3':
                if opt == '1':
                    bet_phase(x)
                if opt == '2':
                    deck, given_cards = card_phase(deck, given_cards, x)
                if opt == '4':
                    print_stats()
                    input("Press enter to continue")
                if opt == '5':
                    deck, given_cards = card_phase(deck, given_cards, x, y="2")
                    opt = '3'
                # Guardamos el NIF del actual banco en una variable
                if not opt == '3':
                    opt = menu(head, menu_ingame_opt)
    # Repartimos puntos
    return_cards(given_cards, deck)
    bank = give_points(bank)


def card_phase(deck, given_cards, x="", y=""):
    if players[x]["human"] is True and y == "":
        if len(players[x]["cards"]) > 0:
            chance = floor(moreThan7_half(players[x]["roundPoints"], deck))
            print("".ljust(54) + "chance of passing 7.5 is: ", chance, "%")
        order = input("".ljust(54) + "{} order card? Y/N".format(players[x]["name"]))
        if order.lower() == "y":
            # Guardamos las cartas que le salen a cada jugador
            players[x]["cards"].append(deck[0])
            # Añadimos el valor de la carta a los puntos de ronda dl jugador
            players[x]["roundPoints"] += mazo[deck[0]]["realValue"]
            # Guardamos en una lista las cartas que han salido
            given_cards.append(deck[0])
            print("".ljust(54) + "The new card is {}".format(mazo[deck[0]]["literal"]))
            # Eliminamos las cartas que salen del mazo
            del deck[0]
            print("".ljust(54) + "Current points:", players[x]["roundPoints"])
            input("Enter to continue".rjust(71))
    else:
        chance = moreThan7_half(players[x]["roundPoints"], deck)
        while chance < players[x]["type"]:
            players[x]["cards"].append(deck[0])
            # Añadimos el valor de la carta a los puntos de ronda dl jugador
            players[x]["roundPoints"] += mazo[deck[0]]["realValue"]
            # Guardamos en una lista las cartas que han salido
            given_cards.append(deck[0])
            # Eliminamos las cartas que salen del mazo
            del deck[0]
            chance = moreThan7_half(players[x]["roundPoints"], deck)
# Devolvemos las cartas que han salido al mazo
    return deck, given_cards


def game_setup():
    # Reseteamos los puntos de los jugadores a 20
    reset_points()
    # Barjamos el mazo antes de establecer prioridades
    deck = barajar_mazo(list(mazo.keys()))
    # Establecemos las prioridades de los jugadores
    given_cards = set_game_priority(deck)
    # Devolvemos las cartas al mazo
    given_cards = []
    # Volvemos a barajar el mazo
    deck = barajar_mazo(deck)
    return deck


def bet_phase(x=""):
    # La banca no apuesta
    if not players[x]["bank"]:
        # Si el jugador es humano, realiza su apuesta manualmente *crear funcion para hacer la apuesta
        if players[x]["human"]:
            print(players[x]["name"], "points:", players[x]["points"])
            players[x]["bet"] = check_valid_bet(players[x]["points"])
        # Funcion que realiza la apuesta de un bot
        else:
            print(players[x]["name"], "points:", players[x]["points"])
            bet_on_risk(x)
    else:
        print("The bank doesnt bet!!!")


def start_game():
    print(context_game["rounds"])
    # Realizamos las configuraciones iniciales
    context_game["mazo"] = game_setup()
    # Realizamos turnos hasta que se terminan las rondas
    print_stats()
    input("Press enter to continue".rjust(78))
    for i in range(0, context_game["rounds"]):
        turn(context_game["mazo"], i)
        # Si no hay almenos 2 jugadores con puntos, termina la partida
        s_players = check_minimum_2_player_with_points()
        if not s_players:
            winner(i)
            reset_cards()
            break
        print_stats()
        opt = input("Press enter start another round, exit to go back: ".rjust(97))
        if opt == "exit":
            break
        if i == context_game["rounds"] - 1:
            winner(i)
            reset_cards()


def return_cards(given_cards, deck):
    # Añadimos las cartas que han salido devuelta al mazo
    for x in given_cards:
        deck.append(x)


def seven_and_half():
    # Funcion que devuleve una lista con los jugadores que tengan 7.5
    lista_siete_y_medio = []
    for x in context_game["game"]:
        if players[x]["roundPoints"] == 7.5:
            lista_siete_y_medio.append(x)
    return lista_siete_y_medio


def give_points(bank):
    # Guardamos los 7.5 en una lista
    contenders = seven_and_half()
    # Creamos una copia invertida de la lista de jugadores para repartir por prioridad
    priority_list = invert_list(context_game["game"])
    # Eliminamos al banco de la lista (ya que este es que da los puntos)
    del priority_list[0]
    # En funcion de las puntuaciones asignamos los puntos en orden de prioridad
    for x in priority_list:
        if bank in contenders:
            players[x]["points"] -= players[x]["bet"]
            players[bank]["points"] += players[x]["bet"]
            if players[x]["points"] == 0:
                print(players[x]["name"], "lost")
        else:
            if x in contenders:
                if players[bank]["points"] > players[x]["bet"]:
                    players[x]["points"] += players[x]["bet"]
                    players[bank]["points"] -= players[x]["bet"]
                else:
                    players[x]["points"] += players[bank]["points"]
                    players[bank]["points"] = 0
            if players[x]["roundPoints"] < 7.5:
                if players[bank]["roundPoints"] < 7.5:
                    if players[x]["roundPoints"] > players[bank]["roundPoints"]:
                        if players[bank]["points"] > players[x]["bet"]:
                            players[x]["points"] += players[x]["bet"]
                            players[bank]["points"] -= players[x]["bet"]
                        else:
                            players[x]["points"] += players[bank]["points"]
                            players[bank]["points"] = 0
                    else:
                        players[x]["points"] -= players[x]["bet"]
                        players[bank]["points"] += players[x]["bet"]
                        if players[x]["points"] == 0:
                            print(players[x]["name"], "lost")
                else:
                    players[x]["points"] += players[x]["bet"]
                    players[bank]["points"] -= players[x]["bet"]
            if players[x]["roundPoints"] > 7.5:
                if players[bank]["roundPoints"] < 7.5:
                    players[x]["points"] -= players[x]["bet"]
                    players[bank]["points"] += players[x]["bet"]
                    if players[x]["points"] == 0:
                        print(players[x]["name"], "lost")
    # En caso de haber un o varios 7.5 que no sean el banco, el que tiene mas prioridad se convierte en el banco
    if len(contenders) > 0 and bank not in contenders:
        players[bank]["bank"] = False
        players[priority_list[0]]["bank"] = True
        print(players[contenders[0]]["name"], "is the new bank")
        bank = priority_list[0]
        # Ajustamos las prioridades de los jugadores de acuerdo al cambio de banco
        priority_adjustment(bank)
        # Devolvemos el nif del banco
        return bank


def priority_adjustment(bank):
    # Eliminamos al banco de la lista, ya que tiene que ser el ultimo independientemente de su prioridad actual
    del context_game["game"][context_game["game"].index(bank)]
    # Ordenamos a los jugadores por prioridad
    for x in context_game["game"]:
        for y in context_game["game"]:
            if players[x]["priority"] > players[y]["priority"]:
                (context_game["game"][context_game["game"].index(x)],
                 context_game["game"][context_game["game"].index(y)]) = \
                    (context_game["game"][context_game["game"].index(y)],
                     context_game["game"][context_game["game"].index(x)])
    # Añadimos al banco en la ultima posicion
    context_game["game"].append(bank)
    # Corregimos las prioridades
    for i in range(0, len(context_game["game"])):
        players[context_game["game"][i]]["priority"] = i + 1


def print_stats():
    os.system("clear")
    print(Seven_and_half, ("*" * 140))
    j = list(players.keys())[0]
    for x in players[j]:
        print("".ljust(35) + str(x).ljust(30), end="")
        for k in context_game["game"]:
            if x == "cards":
                res = ""
                for z in players[k][x]:
                    res += z + ";"
                print(res[0:-1].ljust(30), end="")
            else:
                print(str(players[k][x]).ljust(30), end="")
        print()


def reset_cards():
    for x in context_game["game"]:
        players[x]["cards"] = []


def get_players():
    query = ("SELECT * FROM PLAYER")
    cursorObject.execute(query)
    database.commit()
    result_raw = cursorObject.fetchall()
    result = []
    for x in result_raw:
        result.append(list(x))
    for x in result:
        players[str(x[0])] = {"name": x[1], "human": True, "bank": False, "initialCard": "", "priority": 0,
                "type": x[2], "bet": 0, "points": 0, "cards": [], "roundPoints": 0}
        if x[3] == 0:
            players[x[0]]["human"] = False


def add_players_to_game(x = ""):
    if x == '1':
        os.system("clear")
        print(menu_21)
        print("\n" + "".ljust(46) + ("*" * 10) + "Actual players in game" + ("*" * 10))
        if len(context_game["game"]) == 0:
            print("There is no players in game".rjust(80))
            input("Enter to continue".rjust(75))
        else:
            for x in context_game["game"]:
                print(x.ljust(10), players[x]["name"].ljust(10), end="")
                if players[x]["human"]:
                    print("human".ljust(10), end="")
                else:
                    print("boot".ljust(10), end="")
                if players[x]["type"] == 30:
                    print("Cautious\n")
                elif players[x]["type"] == 40:
                    print("Moderated\n")
                elif players[x]["type"] == 60:
                    print("Bold\n")
    os.system("clear")
    print(menu_21)
    print("Select players".center(140, '*'))
    print("Boot Player".center(68) + "||" + "Human Players".center(68))
    print('-' * 140)
    print("ID".ljust(21) + "Name".ljust(24) + "Type".ljust(23) + "||", end="  ")
    print("ID".ljust(21) + "Name".ljust(24) + "Type")
    print('*' * 140)
    bots = []
    humans = []
    for x in players:
        if players[x]["human"] is False:
            bots.append(x)
        else:
            humans.append(x)
    while len(humans) > 0 or len(bots) > 0:
        if len(bots) > 0:
            print(bots[0].ljust(20), players[bots[0]]["name"].ljust(24), end="")
            if players[bots[0]]["type"] == 30:
                print("Cautious".ljust(23), end="||".ljust(4))
            elif players[bots[0]]["type"] == 40:
                print("Moderate".ljust(23), end="||".ljust(4))
            elif players[bots[0]]["type"] == 60:
                print("Bold".ljust(23), end="||".ljust(4))
            del bots[0]
        else:
            print("".ljust(68), end="||".ljust(4))
        if len(humans) > 0:
            print(humans[0].ljust(20), players[humans[0]]["name"].ljust(24), end="")
            if players[humans[0]]["type"] == 30:
                print("Cautious".ljust(23).ljust(8))
            elif players[humans[0]]["type"] == 40:
                print("Moderate".ljust(23).ljust(8))
            elif players[humans[0]]["type"] == 60:
                print("Bold".ljust(23).ljust(8))
            del humans[0]
        else:
            print()
    print("\n\n" + ("*" * 140))
    opt = input("\n".ljust(39) + "Option ( id to add player, -id to remove player, -1 to exit): \n" + "".ljust(50))
    if len(opt) > 0:
        if opt in players:
            context_game["game"].append(opt)
            print("\n" + "".ljust(46) + ("*" * 10) + "Actual players in game" + ("*" * 10))
            if len(context_game["game"]) == 0:
                print("There is no players in game".rjust(80))
                input("Enter to continue".rjust(75))
            else:
                for x in context_game["game"]:
                    print("".ljust(43) + x.ljust(13), players[x]["name"].ljust(15), end="")
                    if players[x]["human"]:
                        print("human".ljust(10), end="")
                    else:
                        print("boot".ljust(10), end="")
                    if players[x]["type"] == 30:
                        print("Cautious")
                    elif players[x]["type"] == 40:
                        print("Moderated")
                    elif players[x]["type"] == 60:
                        print("Bold")
            input("enter to continue".rjust(71))
            add_players_to_game()
        elif opt[0] == '-' and len(opt) == 10:
            if opt[1:] in context_game["game"]:
                remove = context_game["game"].index(opt[1:])
                del context_game["game"][remove]
                input("Press enter to continue".rjust(71))
                add_players_to_game()
        elif opt == '-1':
            print()
        else:
            print(("=" * 66) + "Invalid Option" + ("=" * 66))
            input("Press enter to continue".rjust(71))
            add_players_to_game()


def winner(rounds):
    os.system("clear")
    print(game_over)
    max = context_game["game"][0]
    for x in context_game["game"]:
        if players[x]["points"] > players[max]["points"]:
            max = x
    print("".ljust(25) + "The winner is", max, "-", players[max]["name"], "in", rounds, "rounds")
    input("Enter to continue".rjust(42))


def deleteplayer():
    for x in delete_players:
        player_id = [x]
        query = ("delete from player where player_id = %s ;")
        cursorObject.execute(query, (player_id))
        database.commit()
