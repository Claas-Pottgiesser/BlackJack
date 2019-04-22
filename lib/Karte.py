class Karte:
    def __init__(self, farbe, wert, name):
        self._farbe = farbe
        self._wert = wert
        self._name = name

    def value(self):
        return self._wert

    def identifier(self):
        return self._farbe + " " + self._name

    