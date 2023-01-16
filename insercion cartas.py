import Paquetes.datos as m
from mysql.connector import *

database = connect(user="gameadmin", password="sieteymedio123$", host="sevenandhalf.mysql.database.azure.com",
                   database="seven_half")
cursorObject = database.cursor(buffered=True)


for i in m.mazo["mazo_default"]:
    if i == "B01":
        print()
    else:
        card_id = i
        card_name = m.mazo["mazo_default"][i]["literal "]
        card_value = m.mazo["mazo_default"][i]["realValue"]

        indice = card_name.index("de") + 3

        card_suit = card_name[indice:]
        card_priority = m.mazo["mazo_default"][i]["priority "]
        card_real_value = m.mazo["mazo_default"][i]["value"]
        deck_id = 1

        print(card_id, card_name, card_value, card_suit, card_priority, card_real_value, deck_id, sep=" | ")
        query = ("INSERT INTO card VALUES(%s, %s, %s, %s, %s, %s, %s)")
        values = [(card_id, card_name, card_value, card_suit, card_priority, card_real_value, deck_id)]
        cursorObject.executemany(query, values)
        database.commit()
database.close()