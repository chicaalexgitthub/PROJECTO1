# Programa principal
import os
import xml.etree.cElementTree as ET
from Paquetes import datos as d
from Paquetes import funciones as f

f.get_players()

flg_0 = True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
flg_05 = False
flg_06 = False
flg_end = False

while not flg_end:
    while flg_0:
        opt = f.menu(d.menu_principal, d.menu_principal_opt)
        if opt == '1':
            flg_0 = False
            flg_01 = True
        if opt == '2':
            flg_0 = False
            flg_02 = True
        if opt == '3':
            flg_03 = True
            flg_0 = False
        if opt == '4':
            flg_04 = True
            flg_0 = False
        if opt == '5':
            flg_05 = True
            flg_0 = False
        if opt == '6':
            f.insert_players()
            f.deleteplayer()
            flg_0 = False
            flg_end = True
    while flg_01:
        opt = f.menu(d.menu_01, d.menu_01_opt)
        if opt == '1':
            f.create_human_player()
        if opt == '2':
            f.create_boot()
        if opt == '3':
            f.show_players()
        if opt == '4':
            flg_01 = False
            flg_0 = True
    while flg_02:
        opt = f.menu(d.menu_02, d.menu_01_opt)
        if opt == '1':
            f.add_players_to_game('1')
        if opt == '2':
            opt = f.menu(d.menu_022, d.menu_022_opt)
            f.get_deck(int(opt))
        if opt == '3':
            d.context_game["rounds"] = f.setMaxRounds()
        if opt == '4':
            flg_02 = False
            flg_0 = True
    while flg_03:
        if f.check_conditions():
            f.start_game()
        flg_03 = False
        flg_0 = True
    while flg_04:
        opt = f.menu(d.menu_04, d.menu_04_opt)
        if opt == '1':
            lista_players = f.getranking("earnings")
            f.print_ranking(lista_players, "E A R N I N G S")
        if opt == '2':
            lista_players = f.getranking("games")
            f.print_ranking(lista_players, "G A M E S")
        if opt == '3':
            lista_players = f.getranking("minutes")
            f.print_ranking(lista_players, "M I N U T E S")
        if opt == '4':
            flg_04 = False
            flg_0 = True
    while flg_05:
        opt = f.menu(d.menu_05, d.menu_05_opt)
        if opt == '1':
            print()
        if opt == '2':
            f.generateXML(["idgame", "idplayer", "maxbet"], "select DISTINCT cardgame_id, player_id, "
                                                                           "bet_points from player_game_round pgr "
                                                                           "where bet_points = (select max(bet_points) "
                                                                           "from player_game_round where cardgame_id = "
                                                                           "pgr.cardgame_id) order by bet_points desc;","highestbet.xml")

            f.print_informes(3, "    ID Game     ID Player        Max Bet ", "select DISTINCT cardgame_id, player_id, "
                                                                           "bet_points from player_game_round pgr "
                                                                           "where bet_points = (select max(bet_points) "
                                                                           "from player_game_round where cardgame_id = "
                                                                           "pgr.cardgame_id) order by bet_points desc;")
        if opt == '3':
            f.generateXML(["cardgame_id", "idplayer", "bet_points"], "select DISTINCT cardgame_id, "
                                                                             "player_id, bet_points from "
                                                                             "player_game_round pgr where bet_points = "
                                                                             "(select min(bet_points) from "
                                                                             "player_game_round where cardgame_id = "
                                                                             "pgr.cardgame_id) order by bet_points asc;",
                          "lowestbet.xml")
            f.print_informes(3, "    ID Game     ID Player        Min Bet ", "select DISTINCT cardgame_id, "
                                                                             "player_id, bet_points from "
                                                                             "player_game_round pgr where bet_points = "
                                                                             "(select min(bet_points) from "
                                                                             "player_game_round where cardgame_id = "
                                                                             "pgr.cardgame_id) order by bet_points asc;")
        if opt == '4':
            print()
        if opt == '5':
            print()
        if opt == '6':
            print()
        if opt == '7':
            f.generateXML(["idgame", "banks"], "select cr.cardgame_id, count(distinct player_id) from cardgame cr join player_game_round"
                             " pgr on cr.cardgame_id = pgr.cardgame_id where is_bank = True group by pgr.cardgame_id;", "bankpergame.xml")
            f.print_informes(2, "ID Game     Different bank",
                             "select cr.cardgame_id, count(distinct player_id) from cardgame cr join player_game_round"
                             " pgr on cr.cardgame_id = pgr.cardgame_id where is_bank = True group by pgr.cardgame_id;")
        if opt == '8':
            f.generateXML(["idgame", "averagebet"], "select card.cardgame_id, sum(bet_points)/count(*) from cardgame card join "
                             "player_game_round pgr on pgr.cardgame_id = card.cardgame_id group by card.cardgame_id;", "averagebetpergame.xml")
            f.print_informes(2, "ID Game     Average Bet",
                             "select card.cardgame_id, sum(bet_points)/count(*) from cardgame card join "
                             "player_game_round pgr on pgr.cardgame_id = card.cardgame_id group by card.cardgame_id;")
        if opt == '9':
            f.generateXML(["idgame","averagebet" ],"select cardgame_id, avg(bet_points) from player_game_round where round_num = 0 group by cardgame_id;","avgfirstround.xml")
            f.print_informes(2, "ID Game     Num Round",
                             "select cardgame_id, avg(bet_points) from player_game_round where round_num = 0 group by cardgame_id;")
        if opt == '10':
            f.generateXML(["idgame", "averagebet"], "select pgr.cardgame_id, avg(bet_points) from player_game_round pgr where round_num = "
                             "(select max(round_num) from player_game_round where cardgame_id = pgr.cardgame_id) "
                             "group by pgr.cardgame_id;", "avglastround.xml")
            f.print_informes(2, "ID Game     Num Round",
                             "select pgr.cardgame_id, avg(bet_points) from player_game_round pgr where round_num = "
                             "(select max(round_num) from player_game_round where cardgame_id = pgr.cardgame_id) "
                             "group by pgr.cardgame_id;")
        if opt == '11':
            flg_05 = False
            flg_0 = True
