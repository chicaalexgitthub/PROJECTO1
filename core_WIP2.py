from Paquetes.funciones import *
from Paquetes.datos import *


def turn(deck):
    given_cards = []
    # Se realizan las apuestas de cada jugador
    bet_phase()
    # Recorremos la lista de jugadores ordenada por prioridad ascendente
    for x in context_game["game"]:
        if players[x]["bank"] is True:
            bank = x
        # Cada jugador pide sus cartas
        card_phase(deck, given_cards, x)
    # Repartimo puntos
    give_points(bank)


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
                players[x]["bet"] = int(input("Whats your bet?: "))
            # Funcion que realiza la apuesta de un bot
            else:
                bet_on_risk(x)


def start_game():
    deck = game_setup()
    turn(deck)


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
    if len(contenders) > 0:
        if bank in contenders:
            # La banca gana todos los puntos
            print()
        else:
            # hay que hacer cambio de banca
            print()



start_game()
