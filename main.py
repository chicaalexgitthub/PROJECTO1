# Programa principal
import os

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
            print()
        if opt == '2':
            print()
        if opt == '3':
            print()
        if opt == '4':
            flg_04 = False
            flg_0 = True
    while flg_05:
        opt = f.menu(d.menu_05, d.menu_05_opt)
        if opt == '1':
            print()
        if opt == '2':
            print()
        if opt == '3':
            print()
        if opt == '4':
            print()
        if opt == '5':
            print()
        if opt == '6':
            print()
        if opt == '7':
            print()
        if opt == '8':
            print()
        if opt == '9':
            print()
        if opt == '10':
            print()
        if opt == '11':
            flg_05 = False
            flg_0 = True
