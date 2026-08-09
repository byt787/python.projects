# my first calculator :3
# only works with 2 numbers for now
zahl1 = float(input("erste zahl eingeben bitti: "))
op = input("(+, -, *, /): ")
zahl2 = float(input("zweite zahl eingeben bitti: "))

# thought about using match case instead of if/elif but was too lazy
if op == "+":
    ergebnis = zahl1 + zahl2
elif op == "-":
    ergebnis = zahl1 - zahl2
elif op == "*":
    ergebnis = zahl1 * zahl2
elif op == "/":
    # gotta watch out for division by zero here or this thing crashes
    if zahl2 == 0:
        print("Dummerchen man kann nd druch 0 teilen :c")
        ergebnis = None
    else:
        ergebnis = zahl1 / zahl2
else:
    print("ne glaub ich nd nimm was richtiges :3")
    ergebnis = None

if ergebnis is not None:
    print("ergebnis ist:", ergebnis)

# todo: maybe add a loop later so you dont have to restart the script every time
# but leaving it like this for now
