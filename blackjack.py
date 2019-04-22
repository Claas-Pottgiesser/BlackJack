from lib.Deck import Deck
from lib.Karte import Karte
from lib.Hand import Hand


def generate_pokerdeck():
    farben = ["Piek", "Kreuz","Herz", "Karo"]
    kartenliste = []
    for farbe in farben:
        for value in range(2,11):
            kartenliste.append(Karte(farbe, value, str(value)))
        for name in ["King", "Queen", "Jack"]:
            kartenliste.append(Karte(farbe,10,name))
        kartenliste.append(Karte(farbe,11,"Ass"))
    return kartenliste

def gewinner(spieler_hand_value, dealer_hand_value):
    if spieler_hand_value == dealer_hand_value:
        return "Draw... wie öde."
    elif 21 >= spieler_hand_value > dealer_hand_value:
        return "Spieler gewinnt!"
    elif 21 <= spieler_hand_value < dealer_hand_value:
        return "Spieler gewinnt!"
    elif dealer_hand_value > 21 >= spieler_hand_value
        return "Spieler gewinnt!"
    else:
        return "Dealer gewinnt!"


def game():
    deck = Deck()
    deck.initialize(generate_pokerdeck())
    rundencounter = 0
    while deck.cardcount() > 10:
        rundencounter += 1
        print("Das ist jetzt die " + str(rundencounter) + ". Runde!")
        einzelspiel(deck)

def einzelspiel(deck):    
    dealerhand = Hand()
    spielerhand = Hand()
    for i in (1,2):
        spielerhand.add_card(deck.draw())
        dealerhand.add_card(deck.draw())
        if i == 1:
            print("Dealerhand:")
            dealerhand.print()

    while spielerhand.value() < 21:
        print("Spielerhand (" + str(spielerhand.value()) + ")")
        spielerhand.print()
        print("Moechtest Du eine Karte ziehen? j/N")
        ziehen=input()
        if ziehen.lower() != "j" and ziehen.lower() != "y":
            break
        spielerhand.add_card(deck.draw())

    while dealerhand.value() < 17:
        dealerhand.add_card(deck.draw())
    print_result(spielerhand,dealerhand)

def print_result(spielerhand, dealerhand):
    print("Dealer \t|Spieler\n----------------------------")
    print(str(dealerhand.value()) + "\t|" + str(spielerhand.value()) + "\n----------------------------")
    print(gewinner(spielerhand.value(),dealerhand.value()))
    print("Dealerhand:")
    dealerhand.print()
    print()
    print("Spielerhand:")
    spielerhand.print()

    # print("Dealerhand:")
    # print(dealerhand.value())
    # dealerhand.print()    
    # print("Spielerhand:")
    # print(spielerhand.value())
    # spielerhand.print()

if __name__ == "__main__":
    game()