# number guessing game
# computer picks a random number i have to guess it

import random

geheimzahl = random.randint(1, 100)
versuche = 0
geraten = False

print("zahl zwischen 1 und 100 erraten ^-^")

# using a while loop because i dont know beforehand how many guesses the user needs
while not geraten:
    eingabe = input("dein guess?: ")

    # if someone types letters instead of numbers this shouldnt crash the script
    if not eingabe.isdigit():
        print("wixxa du musst ne zahl eingeben :c")
        continue

    tipp = int(eingabe)
    versuche = versuche + 1

    if tipp < geheimzahl:
        print("zu niedrig, nochmal :3")
    elif tipp > geheimzahl:
        print("zu hoch, nochmal :3")
    else:
        geraten = True
        print("Yessss du hast nur", versuche, "versuche gebraucht ^-^")

# little rating at the end, makes it more fun i think
if versuche <= 5:
    print("crazy shit")
elif versuche <= 10:
    print("kann man machen ig")
else:
    print("opfer xD")
