from Paquetes.funciones import *
from Paquetes.datos import *

deck = list(mazo.keys())


def start_game():
    deck = barajar_mazo(list(mazo.keys()))
    given_cards = set_game_priority(deck)
    reset_points()
    establish_bank()
    bank = None
    for x in context_game["game"]:
        if players[x]["bank"] is True:
            bank = x
    for i in range(0, len(context_game)):
        d.players[context_game["game"][i]]["priority"] = i + 1
    print(players)
    given_cards = []
    deck = barajar_mazo(deck)
    for x in context_game["game"]:
        if players[x]["bank"] is True:
            print(players[x]["name"], "is the bank")
        else:
            bet_on_risk(context_game["game"])
    for x in context_game["game"]:
        print(players[x]["name"] + " bet =", players[x]["bet"])
    for x in context_game["game"]:
        order = "Y"
        cards = []
        while order == "Y" or order == "y":
            order = input("{} order card? Y/N".format(players[x]["name"]))
            if order.lower() == "y":
                cards.append(deck[0])
                players[x]["roundPoints"] += mazo[deck[0]]["realValue"]
                given_cards.append(deck[0])
                print("The new card is {}".format(deck[0]))
                del deck[0]
                print(players[x]["roundPoints"])
    for x in given_cards:
        deck.append(x)
    deck = barajar_mazo(deck)
    for x in context_game["game"]:
        if players[bank]["roundPoints"] == 7.5:
            if not players[x]["roundPoints"] == 7.5:
                print(players[x]["name"], "loses", players[x]["bet"])
                players[bank]["points"] += players[x]["bet"]
                players[x]["points"] -= players[x]["bet"]
        elif players[bank]["roundPoints"] < 7.5:
            if x != bank:
                if players[bank]["roundPoints"] < players[x]["roundPoints"]:
                    print(players[x]["name"], "loses", players[x]["bet"])
                    players[bank]["points"] += players[x]["bet"]
                    players[x]["points"] -= players[x]["bet"]
                else:
                    print(players[bank]["name"], "loses", players[x]["bet"])
                    players[x]["points"] += players[x]["bet"]
                    players[bank]["points"] -= players[x]["bet"]
        else:
            if players[x]["roundPoints"] < players[bank]["roundPoints"] and players[x]["roundPoints"] < 7.5:
                players[x]["points"] += players[x]["bet"]
                players[bank]["points"] -= players[x]["bet"]
    print(players)


start_game()

