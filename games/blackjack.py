import random
from games  import helper
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# RANKS = ["A", "2", "3", "4"]


deck = [f"{s} {r}" for s in SUITS for r in RANKS]
def play_blackjack(saldo):
    while True:
        welkom_text()
        choice = input("Wil je blackjack spelen? J/N ")
        if choice.lower() == "n":
            print(f"Huidige saldo is : {saldo}")
            break
        inzet = helper.neem_bod(saldo)
        saldo -= inzet
        dealer_hand = []
        speler_hand = []

        # In het begin krijg iedereen 2 kaarten
        kaart = krijg_kart(deck)
        deck.remove(kaart)
        speler_hand.append(kaart)

        kaart = krijg_kart(deck)
        deck.remove(kaart)
        speler_hand.append(kaart)

        kaart = krijg_kart(deck)
        deck.remove(kaart)
        dealer_hand.append(kaart)

        kaart = krijg_kart(deck)
        deck.remove(kaart)
        dealer_hand.append(kaart)


        totaal_speler = totaal_berekenen(speler_hand)
        print(speler_hand)
        print(totaal_speler)
        while True:
            # We zien alleen eerste kaart van dealer, andere kaart is verborgen
            print(f"Dealer heeft [{dealer_hand[1]}, XX] ")
            print(f"Je hebt {speler_hand}")
            choice = input("Hit of Stand?").lower()
            if choice == "hit":
                kaart = krijg_kart(deck)
                deck.remove(kaart)
                speler_hand.append(kaart)
                totaal_speler = totaal_berekenen(speler_hand)
                print(len(deck))
                if totaal_speler > 21:
                    print(speler_hand)
                    print(f"Je hebt {totaal_speler} dus {inzet} € verloren ")
                    break
                continue
            elif choice == "stand":
                break
            else :
                print("Type 'Hit' of 'Stand'")
                continue

        if totaal_speler > 21:
            continue

        totaal_dealer = totaal_berekenen(dealer_hand)

        while totaal_dealer < 17 :
            kaart = krijg_kart(deck)
            deck.remove(kaart)
            dealer_hand.append(kaart)
            totaal_dealer = totaal_berekenen(dealer_hand)
            if totaal_dealer > 21:
                print(f"Dealer hand : {dealer_hand}")
                print(f"Dealer heeft {totaal_dealer} dus je hebt {inzet}€ gewonnen")
                saldo += inzet*2
                break
        if totaal_dealer > 21:
            continue
        print(f"Je hebt {totaal_speler} {speler_hand}")
        print(f"Dealer heeft {totaal_dealer}  {dealer_hand}")

        winnaar = winnaar_berekenen(totaal_speler, totaal_dealer)

        if winnaar == "speler":
            print(f"Je hebt {inzet} gewonnen")
            saldo += inzet * 2
        elif winnaar == "dealer" :
            print(f"Dealer heeft gewonnen dus {inzet} € verloren ")
        elif winnaar == "draw":
            print("Het is draw")
            # inzet terug naar saldo
            saldo += inzet
    return saldo

def welkom_text():
    print("""
Casino de Gouden Driehoek - Blackjack
-----------------------------------        
        """)

def krijg_kart(deck):
    # neem de kaart
    return deck[random.randint(0,len(deck)-1)]

def totaal_berekenen(hand):
    totaal = 0
    a_count = 0
    for i in hand:
        if i[-1] in ["Q","K","J","0"]:
            totaal += 10
        elif i[-1] == "A":
            a_count += 1
            totaal += 11
        else:
            totaal += int(i[-1])
    if (a_count > 0) and (totaal > 21):
        totaal -= 10
        if (a_count > 1) and totaal > 21:
            totaal -= 10
            if (a_count > 2) and totaal > 21:
                totaal -= 10
                if (a_count > 3) and totaal > 21:
                    totaal -= 10
    return totaal

def winnaar_berekenen(totaal_speler, totaal_dealer):
    winnaar = ""
    if totaal_dealer > totaal_speler:
        winnaar = "dealer"
    elif totaal_dealer < totaal_speler :
        winnaar = "speler"
    elif totaal_dealer == totaal_speler:
        winnaar = "draw"
    return winnaar

