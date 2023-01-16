from Paquetes.funciones import *
from Paquetes.datos import *


def turn(deck):
    reset_roundPoints()
    given_cards = []
    # Se realizan las apuestas de cada jugador
    bet_phase()
    # Recorremos la lista de jugadores ordenada por prioridad ascendente
    for x in context_game["game"]:
        if players[x]["bank"] is True:
            bank = x
        # Cada jugador pide sus cartas
        print(players[x]["name"], "turn:")
        card_phase(deck, given_cards, x)
    # Repartimo puntos
    bank = give_points(bank)


def card_phase(deck, given_cards, nif):
    deck = barajar_mazo(deck)
    order = "Y"
    cards = []
    while order == "Y" or order == "y":
        order = input("{} order card? Y/N".format(players[nif]["name"]))
        if order.lower() == "y":
            cards.append(deck[0])
            players[nif]["roundPoints"] += mazo[deck[0]]["realValue"]
            given_cards.append(deck[0])
            print("The new card is {}".format(deck[0]))
            del deck[0]
            print(players[nif]["roundPoints"])
    return_cards(given_cards, deck)


def boot_turn():
    deck = barajar_mazo(list(mazo.keys()))


def bank_turn():
    deck = barajar_mazo(list(mazo.keys()))


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
                players[x]["bet"] = int(input(players[x]["name"] + " whats your bet?: "))
            # Funcion que realiza la apuesta de un bot
            else:
                print(players[x]["name"], "points:", players[x]["points"])
                bet_on_risk(x)


def start_game():
    deck = game_setup()
    for i in range(0, rounds):
        turn(deck)
        s_players = check_minimum_2_player_with_points()
        if not s_players:
            break


def return_cards(given_cards, deck):
    for x in given_cards:
        deck.append(x)


def seven_and_half():
    lista_siete_y_medio = []
    for x in context_game["game"]:
        if players[x]["roundPoints"] == 7.5:
            lista_siete_y_medio.append(x)
    return lista_siete_y_medio


def give_points(bank):
    contenders = seven_and_half()
    priority_list = invert_list(context_game["game"])
    del priority_list[0]
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
    if len(contenders) > 0 and bank not in contenders:
        players[bank]["bank"] = False
        players[priority_list[0]]["bank"] = True
        bank = priority_list[0]
        priority_adjustment(bank)
        return bank


def priority_adjustment(bank):
    del context_game["game"][context_game["game"].index(bank)]
    for x in context_game["game"]:
        for y in context_game["game"]:
            if players[x]["priority"] > players[y]["priority"]:
                context_game["game"][context_game["game"].index(x)], \
                context_game["game"][context_game["game"].index(y)] = \
                    context_game["game"][context_game["game"].index(y)], \
                    context_game["game"][context_game["game"].index(x)]
    context_game["game"].append(bank)
    for i in range(0, len(context_game["game"])):
        players[context_game["game"][i]]["priority"] = i + 1


start_game()
