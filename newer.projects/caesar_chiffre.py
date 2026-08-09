# caesar cipher, an old school way of encrypting text by just shifting
# every letter by a fixed number of positions in the alphabet
# example: "a" shifted by 3 becomes "d"

import string

def verschluesseln(text, verschiebung):
    ergebnis = ""

    for zeichen in text:
        if zeichen.isalpha():
            # need to know if its upper or lower case to shift within
            # the right range, otherwise capital letters get messed up
            basis = ord('A') if zeichen.isupper() else ord('a')

            # this is the actual shifting logic, the % 26 makes sure we
            # wrap around back to 'a' after 'z' instead of going into
            # weird ascii symbols
            neuer_code = (ord(zeichen) - basis + verschiebung) % 26 + basis
            ergebnis += chr(neuer_code)
        else:
            # numbers, spaces, punctuation etc just stay the same
            ergebnis += zeichen

    return ergebnis


def entschluesseln(text, verschiebung):
    # decrypting is literally just encrypting with the negative shift
    # took me a second to realize i dont need a whole separate function
    return verschluesseln(text, -verschiebung)


if __name__ == "__main__":
    modus = input("verschluesseln oder entschluesseln? (v/e): ")
    text = input("text eingeben: ")
    shift = int(input("verschiebung (zb 3): "))

    if modus == "v":
        neuer_text = verschluesseln(text, shift)
        print("verschluesselt:", neuer_text)
    elif modus == "e":
        neuer_text = entschluesseln(text, shift)
        print("entschluesselt:", neuer_text)
    else:
        print("bitte v oder e eingeben")

# ist natuerlich keine echte sicherheit, jeder erstsemester kann das mit
# 26 versuchen knacken (brute force). ist halt nur zum lernen wie
# verschluesselung im prinzip funktioniert, nicht fuer echte passwoerter nutzen
