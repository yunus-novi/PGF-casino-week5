import random
from games import helper

def play_fruitmachine(saldo):
    while True:
        welkom_text()
        choice = input("Wil je fruitmachine spelen? J/N ")
        if choice.lower() == "n":
            print(f"Huidige saldo is : {saldo}")
            break
        inzet = helper.neem_bod(saldo)
        saldo -= inzet

        line_1, line_2, line_3 = determine_rols()
        set_line = {line_1, line_2, line_3} # set houd alleen unieke waardes
        print(f"  {line_1}  -  {line_2}  -  {line_3}", end="\n\n")
        if len(set_line) == 1:
            # Alle rollen zijn hetzelfde
            saldo = helper.resultaat_positief(saldo, inzet*3)

        elif len(set_line) == 2:
            # Twee hetzelfde
            saldo = helper.resultaat_positief(saldo, inzet)

        elif len(set_line) == 3:
            # Drie verschillinde
            helper.resultaat_negatief(saldo, inzet)

    return saldo
def determine_rols():
    line_1 = random.choice(["kers","citroen", "ster"])
    line_2 = random.choice(["kers","citroen", "ster"])
    line_3 = random.choice(["kers","citroen", "ster"])

    return line_1, line_2, line_3

def welkom_text():
    print("""
Casino de Gouden Driehoek - Fruitmachine
-----------------------------------        
    """)

