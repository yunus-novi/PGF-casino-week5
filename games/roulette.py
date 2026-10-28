import random
from games import helper


def opties_printen():
    choice = int(input("""
Casino de Gouden Driehoek - Roulette
-----------------------------------
1- Rood
2- Zwart
3- Even
4- Oneven
5- Nummer
0- Terug

Kies je gok : 
    """))
    return choice

def welkom_text():
    print("""
Casino de Gouden Driehoek - Roulette
-----------------------------------        
    """)

def play_roulette(saldo) :
    opties = {1: "rood", 2: "zwart", 3: "even", 4: "oneven", 5:int()}

    while True:

        welkom_text()
        choice = input("Wil je blackjack spelen? J/N ")
        if choice.lower() == "n":
            print(f"Huidige saldo is : {saldo}")
            break

        opties[5] = int() # Reset de gekozen nummer
        choice = opties_printen()
        if choice == 0:
            break
        elif choice > 5 or choice < 0:
            print("Kies aub. een van de gegeven optie! ")
            continue

        if choice == 5:
            nummer = int(input("Welke nummer wil je kiezen? (1-36) "))

            if nummer not in range(0,37):
                print("Kies een juiste nummer! ")
                continue
            else :
                opties[5] = nummer
                break


        inzet = helper.neem_bod(saldo)
        saldo -= inzet
        color, even_oneven, spin = ball_gooien()
        print(f"De bal falt op {color} ({spin})")

        if spin == opties[choice]:
            # Positief x 36
            saldo = helper.resultaat_positief(saldo,inzet*36)

        elif opties[choice] == color or opties[choice] == even_oneven:
            # Positief x 2
            saldo = helper.resultaat_positief(saldo, inzet*2)
        else:
            # Negatief
            helper.resultaat_negatief(saldo, inzet)

            if saldo <= 0:
                print("Helaas is de saldo onvoldoende voor toegang tot een andere game")
                exit(1)

    return saldo


def ball_gooien() :
    spin = random.randint(0, 37)
    if spin == 0:
        color = "groen"
        even_oneven = None
    elif spin <= 18:
        if spin % 2 == 1:
            color = "rood"
            even_oneven = "oneven"
        else:
            color = "zwart"
            even_oneven = "even"
    else:
        if spin % 2 == 0:
            color = "rood"
            even_oneven = "even"
        else:
            color = "zwart"
            even_oneven = "oneven"
    return color, even_oneven, spin