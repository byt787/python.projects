# password generator, needed this because i always use some dumb password and cant think of a good one
# which is obviously not very secure

import random
import string

# collecting all the characters i want to use here
buchstaben = string.ascii_letters  # this gives upper AND lower case automatically, perfect for me
zahlen = string.digits
sonderzeichen = "!@#$%&*?"

alle_zeichen = buchstaben + zahlen + sonderzeichen

laenge = int(input("wie lang soll's werden :3 : "))

# if someone enters 0 or a negative number it shouldnt break everything
if laenge < 1:
    print("musst schon at least 1 zeichen haben xD")
else:
    passwort = ""
    for i in range(laenge):
        passwort = passwort + random.choice(alle_zeichen)

    print("dein neues passwort ^-^ :", passwort)

    # small check if theres at least 1 number in there, not perfect but better than nothing
    hat_zahl = False
    for zeichen in passwort:
        if zeichen in zahlen:
            hat_zahl = True

    if not hat_zahl:
        print("dings da is jetzte keine Zahl drin zahlen sind geil für pw :3")

# maybe ill add an option later to choose if you want special characters or not
# but this is enough for now
