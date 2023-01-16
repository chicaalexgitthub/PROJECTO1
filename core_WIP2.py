from Paquetes.funciones import *
from Paquetes.datos import *


def turn(deck):
    reset_roundPoints()
    given_cards = []
    # Se realizan las apuestas de cada jugador
    bet_phase()
    # Recorremos la lista de jugadores ordenada por prioridad ascendente
    for x in context_game["game"]:
        # Guardamos el NIF del actual banco en una variable
        if players[x]["bank"] is True:
            bank = x
    # Cada jugador pide sus cartas
    card_phase(deck, given_cards)
    # Repartimos puntos
    bank = give_points(bank)


def card_phase(deck, given_cards):
    # Barjamos el mazo
    deck = barajar_mazo(deck)
    for x in context_game["game"]:
        order = "Y"
        print(players[x]["name"], "turn:")
        # Damos cartas hasta que el jugador las rechaze
        while order == "Y" or order == "y":
            order = input("{} order card? Y/N".format(players[x]["name"]))
            if order.lower() == "y":
                # Guardamos las cartas que le salen a cada jugador
                players[x]["cards"].append(deck[0])
                # Añadimos el valor de la carta a los puntos de ronda dl jugador
                players[x]["roundPoints"] += mazo[deck[0]]["realValue"]
                # Guardamos en una lista las cartas que han salido
                given_cards.append(deck[0])
                print("The new card is {}".format(deck[0]))
                # Eliminamos las cartas que salen del mazo
                del deck[0]
                print(players[x]["roundPoints"])
    # Devolvemos las cartas que han salido al mazo
    return_cards(given_cards, deck)


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


def bet_phase():
    for x in context_game["game"]:
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


def start_game():
    # Realizamos las configuraciones iniciales
    deck = game_setup()
    # Realizamos turnos hasta que se terminan las rondas
    for i in range(0, rounds):
        turn(deck)
        # Si no hay almenos 2 jugadores con puntos, termina la partida
        s_players = check_minimum_2_player_with_points()
        if not s_players:
            break


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


start_game()
