import random

def neem_bod(saldo):
    while True:
        inzet = int(input("Hoeveel wil je inzetten? € "))
        if inzet < 0:
            print("Inzet kan niet 0 of lager dan 0 zijn")

        elif inzet > saldo:
            print(f"U mag maximaal {saldo} € inzetten")
            continue
        else:
            break
    return inzet
def resultaat_positief(saldo, winst):
    print(f"Gefeliciteerd je hebt {winst} € gewonnen")
    print(f"Nieuw saldo is {saldo+winst}")
    return saldo+winst
def resultaat_negatief(saldo, los):
    print(f"Helaas je hebt {los} € verloren")
    print(f"Nieuw saldo is {saldo}")