# linked list, this is more of a "understand how data structures work
# under the hood" exercise than something i'd actually use day to day
# since python lists already do all of this for you lol

class Knoten:
    # a single node just holds a value and a pointer to the next node
    def __init__(self, wert):
        self.wert = wert
        self.naechster = None


class VerketteteListe:
    def __init__(self):
        # kopf = the very first node in the list, None means empty list
        self.kopf = None

    def anhaengen(self, wert):
        neuer_knoten = Knoten(wert)

        # if the list is empty, the new node just becomes the head
        if self.kopf is None:
            self.kopf = neuer_knoten
            return

        # otherwise walk all the way to the end and attach it there
        # this "walking" part is what confused me the most at first
        aktueller = self.kopf
        while aktueller.naechster is not None:
            aktueller = aktueller.naechster

        aktueller.naechster = neuer_knoten

    def entfernen(self, wert):
        # special case: removing the head itself
        if self.kopf is not None and self.kopf.wert == wert:
            self.kopf = self.kopf.naechster
            print(f"{wert} entfernt (war der kopf)")
            return

        # otherwise look one step ahead so we can "skip over" the node
        # we want to delete by reconnecting the pointers
        aktueller = self.kopf
        while aktueller is not None and aktueller.naechster is not None:
            if aktueller.naechster.wert == wert:
                aktueller.naechster = aktueller.naechster.naechster
                print(f"{wert} entfernt")
                return
            aktueller = aktueller.naechster

        print(f"{wert} war gar nicht in der liste")

    def anzeigen(self):
        werte = []
        aktueller = self.kopf

        # again just walking through node by node and collecting the values
        while aktueller is not None:
            werte.append(str(aktueller.wert))
            aktueller = aktueller.naechster

        if werte:
            print(" -> ".join(werte))
        else:
            print("liste ist leer")


if __name__ == "__main__":
    liste = VerketteteListe()
    liste.anhaengen(5)
    liste.anhaengen(12)
    liste.anhaengen(7)
    liste.anhaengen(3)

    print("liste:")
    liste.anzeigen()

    liste.entfernen(12)
    print("nach dem entfernen:")
    liste.anzeigen()

    liste.entfernen(999)  # existiert nicht, testet den fehlerfall

# fun fact gelernt: das ist der grund warum "in der mitte einfuegen" bei
# linked lists schneller sein kann als bei normalen listen, weil man nicht
# alles verschieben muss sondern nur 2 pointer umbiegt
# bei mir hier fehlt "einfuegen an bestimmter stelle" noch, vielleicht spaeter
