from random import shuffle

class Deck:
    def __init__(self):
        self._karten = []

    def initialize(self,karten):
        self._karten = karten
        self.shuffle()

    def shuffle(self):
        shuffle(self._karten)

    def draw(self):
        return self._karten.pop(0)

    def print(self):
        for karte in self._karten:
            print(karte.identifier()) 

    def cardcount(self):
        return len(self._karten)