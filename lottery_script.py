import json
import random
import sys

import email_message_template
# import mail_handler
import mail_handler

NUMBER = 0
while True:
    print(f"Trying to draw all people ... {NUMBER}")

    with open("people_data.json", encoding="utf-8") as file:
        SETTINGS_DATA = json.load(file)

    LISTA_LUDZI = list(SETTINGS_DATA["people"].keys())
    NIEPOSORTOWANA_LISTA_LUDZI = LISTA_LUDZI[:]
    # Sortowanie LISTA_LUDZI.
    random.shuffle(LISTA_LUDZI)

    MAILE_LUDZI = {person[0]: person[1]["email"] for person in SETTINGS_DATA["people"].items()}

    WYKLUCZENIA = {person[0]: person[1]["excluded"] for person in SETTINGS_DATA["people"].items()}

    WYLOSOWANE_PARY = {}

    ZBIOR_WYLOSOWANYCH_OSOB = []

    for kupuje_prezent in NIEPOSORTOWANA_LISTA_LUDZI:
        # print(f"[START] Losuje: {kupuje_prezent}.")
        # print(f"Zostały osoby: {set(LISTA_LUDZI) - set(ZBIOR_WYLOSOWANYCH_OSOB)}")
        for tej_osobie in LISTA_LUDZI:

            # 1. Wykluczenia.
            # 2. Nie kupujemy komus 2 razy.
            # 3. Sobie nie kupujemy.
            if WYKLUCZENIA.get(kupuje_prezent) == tej_osobie \
                    or tej_osobie in ZBIOR_WYLOSOWANYCH_OSOB \
                    or kupuje_prezent == tej_osobie:
                continue

            # Przypisz pare sobie.
            WYLOSOWANE_PARY[kupuje_prezent] = tej_osobie
            # Dodaj do zbioru, zeby nie powtarzac.
            ZBIOR_WYLOSOWANYCH_OSOB.append(tej_osobie)
            # print(f"[KONIEC]{kupuje_prezent} wylosowal {tej_osobie}.")
            break
        else:
            pass
            # print(f"[KONIEC]{kupuje_prezent} nie kupuje nikomu.")

    if len(LISTA_LUDZI) > len(WYLOSOWANE_PARY):
        print("Ktoś został pominięty :(. Od początku !")
        NUMBER += 1
        continue

    # print("Prezenty, losowania!")
    for losujacy, wylosowany in WYLOSOWANE_PARY.items():
        # print(f"Kupuje {losujacy} dla  {wylosowany}")

        if MAILE_LUDZI[losujacy]:
            msg = email_message_template.get_email_for(losujacy, MAILE_LUDZI[losujacy], wylosowany, money_limit=200,
                                                       sex=SETTINGS_DATA['people'][losujacy]['sex'])
            mail_handler.HANDLER.send_email("Swiety Mikolaj - Dyspozytornia", MAILE_LUDZI[losujacy], msg.as_string())

    # print("KONIEC !")
    sys.exit()
