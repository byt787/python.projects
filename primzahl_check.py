# checks if a number is a prime number or not
# prime = only divisible by 1 and itself 

zahl = int(input("welche zahl willst du testen? :3 : "))

ist_prim = True

# 0 and 1 (and negative numbers) are no real prime numbers
# i forgot this at first and my script said 1 was prime, which was wrong
if zahl < 2:
    ist_prim = False
else:
    # technically you only need to check up to the square root of zahl
    # but im too stupid to figure out how to do that
    for i in range(2, zahl):
        if zahl % i == 0:
            ist_prim = False
            break  # stops 

if ist_prim:
    print(zahl, "ist nh primzahl ^-^")
else:
    print(zahl, "ist KEINE primzahl :c")

# need to look into how that square root thing works exactly :3
#@milka_161
