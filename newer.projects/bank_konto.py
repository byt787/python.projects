# little bank account simulation, wanted to try classes finally
# this is basically my first real oop attempt lol

class Bankkonto:
    def __init__(self, inhaber, kontostand=0):
        self.inhaber = inhaber
        self.kontostand = kontostand
        # keeping a list of everything that happens so i can print a history later
        self.verlauf = []

    def einzahlen(self, betrag):
        # negative amounts dont make sense for a deposit, block that
        if betrag <= 0:
            print("betrag muss groesser als 0 sein")
            return

        self.kontostand += betrag
        self.verlauf.append(f"einzahlung: +{betrag}")
        print(f"{betrag} eingezahlt, neuer kontostand: {self.kontostand}")

    def abheben(self, betrag):
        if betrag <= 0:
            print("betrag muss groesser als 0 sein")
            return

        # this was the whole point of building this, learning how to prevent
        # withdrawing more money than you actually have
        if betrag > self.kontostand:
            print("nicht genug geld auf dem konto, abbruch")
            return

        self.kontostand -= betrag
        self.verlauf.append(f"abhebung: -{betrag}")
        print(f"{betrag} abgehoben, neuer kontostand: {self.kontostand}")

    def kontostand_anzeigen(self):
        print(f"{self.inhaber} hat aktuell {self.kontostand} auf dem konto")

    def verlauf_anzeigen(self):
        print(f"verlauf von {self.inhaber}:")
        if not self.verlauf:
            print("  (noch nichts passiert)")
        for eintrag in self.verlauf:
            print("  -", eintrag)


# kleiner test lauf, kann man auskommentieren wenn mans nicht braucht
if __name__ == "__main__":
    mein_konto = Bankkonto("milka", 100)
    mein_konto.kontostand_anzeigen()
    mein_konto.einzahlen(50)
    mein_konto.abheben(30)
    mein_konto.abheben(1000)  # sollte fehlschlagen, teste den fehlerfall extra
    mein_konto.verlauf_anzeigen()

# todo: vielleicht spaeter noch ne "ueberweisen" methode zwischen 2 konten bauen
# das ist bestimmt bisschen tricky weil man ja 2 objekte gleichzeitig aendern muss
