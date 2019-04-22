class Hand:
    def __init__(self):
        self._karten = []

    def add_card(self,karte):
        self._karten.append(karte)

    def value(self):
        summe = 0
        ass_counter=0
        for karte in self._karten:
            if karte.value() == 11:
                ass_counter += 1    
            summe = summe + karte.value()
        while summe > 21 and ass_counter > 0:
            summe -= 10
            ass_counter -= 1        
        return summe

    def print(self):
        for karte in self._karten:
            print(karte.identifier()) 