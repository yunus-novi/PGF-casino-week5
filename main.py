from games import blackjack, fruitmachine, roulette
MIN_AGE = 18
HUIDIGE_JAAR = 2026
# Vaste kosten (vk)
VK_DRANKJE = 5
VK_BELASTING = 2
VK_TOEGANG_FEE = 3
TOTAAL_VASTE_KOSTEN = VK_BELASTING + VK_DRANKJE + VK_TOEGANG_FEE




def check_age(datum):
    """
    Haal geboortedatunm in een specifiek formaat en controleer of het goed is
    """
    while True:
        if datum.count("-") == 2:
            gb_dag, gb_maand, gb_jaar = datum.split('-')
            gb_dag = int(gb_dag)
            gb_maand = int(gb_maand)
            gb_jaar = int(gb_jaar)
            if gb_dag > 31 or gb_maand > 12 or gb_jaar > HUIDIGE_JAAR:
                print("Datum format klopt niet!")
                continue
            elif HUIDIGE_JAAR - gb_jaar < MIN_AGE:
                print("U moet minimaal 18 jaar zijn om toegang te krijgen")
                exit(1)
            break
        else:
            print("Datum format klopt niet!")
            exit(1)
    return datum

def calculate_age(datum):
    return HUIDIGE_JAAR - int(datum.split("-")[-1])

def determine_salutation(geslacht: str) -> str:
    if geslacht in ["man", "men", "boy", "jongen"]:
        greeting = "Meneer"
    elif geslacht in ["vrouw", "female", "girl", "meisje"]:
        greeting = "Mevrouw"
    else:
        greeting = "Beste"
    return greeting

def show_welcome_message(achternaam: str, budget: float, greeting: str, saldo: float | int):
    print(f"""
Casino de Gouden Driehoek
----------------------------------------
Welkom {greeting} {achternaam.title()}

Startbudget:    € {budget}
Vaste kosten:   € {TOTAAL_VASTE_KOSTEN}
Saldo:          € {saldo}

    """)

def welkom_klant():
    """
    Dit welkom de klant en haal gegevens
    """
    print("Welkom naar Casino de Gouden Driehoek")
    naam = input("Wat is je naam : ").lower().title()
    achternaam = input("Wat is je achternaam : ").lower().title()

    # geboorte datum validatie
    birthdate = check_age(input("Wat is je geboortedatum? (dd-mm-jjjj) : "))
    age = calculate_age(birthdate)

    greeting = determine_salutation(input("Geslacht : ").lower())
    budget = float(input("Start Budget(€) : "))

    return naam, achternaam, greeting, budget, age, birthdate

def calculate_saldo(budget: float):
    saldo = budget - TOTAAL_VASTE_KOSTEN
    return saldo

def choose_game():
    game = int(input('''
Casino de Gouden Driehoek - Spellen
-----------------------------------
1. Roulette
2. Fruit
3. Blackjack
0. Terug

Kies een optie : 
'''))
    return game

def hoofdmenu():
    hm_choice = int(input("""
Casino de Gouden Driehoek - hoofdmenu
-------------------------------------
1-Spelen
2-Saldo zien
3-Account gegevens zien
0-Stop

Kies een optie : 
"""))
    return hm_choice

def saldo_weergave(saldo):
    print(f"Huidig saldo: € {saldo:.2f}")

def accountgegevens_weergave(naam, achternaam, age, greeting, birthdate):
    print(f"""
Casino de Gouden Driehoek - Accoutgegevens
-----------------------------------
Naam :{naam.title()} {achternaam.title()}
Aansprekvorm : {greeting} 
Geboortedatum : {birthdate}
Age : {age}
""")
    pass

def main():
    naam, achternaam, greeting, budget, age, birthdate= welkom_klant()
    saldo = calculate_saldo(budget)
    show_welcome_message(achternaam, budget, greeting, saldo)

    while True:
        input("Druk enter om door te gaan... ")
        match hoofdmenu():
            case 0:
                exit(1)
            case 1:
                while True:
                    game = choose_game()
                    if game not in range(4):
                        print("Kies een van de game!")
                        continue
                    elif game == 1:
                        saldo = roulette.play_roulette(saldo)
                    elif game == 2:
                        saldo = fruitmachine.play_fruitmachine(saldo)
                    elif game == 3:
                        saldo = blackjack.play_blackjack(saldo)
                    elif game == 0:
                        break
            case 2:
                saldo_weergave(saldo)
            case 3:
                accountgegevens_weergave(naam, achternaam, age, greeting, birthdate)
            case _:
                print("Kies een van de gegeven optie! ")
                continue


main()