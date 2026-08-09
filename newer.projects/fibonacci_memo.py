# fibonacci with memoization, this took me a while to actually understand
# normal recursive fibonacci is SUPER slow for bigger numbers because it
# recalculates the same values over and over again

import time

# this dict remembers results we already calculated so we dont do the
# same work twice, this is basically what "memoization" means i think
cache = {}

def fib_langsam(n):
    # the slow version without caching, just for comparison later
    if n <= 1:
        return n
    return fib_langsam(n - 1) + fib_langsam(n - 2)


def fib_schnell(n):
    # check cache first before doing any actual calculation
    if n in cache:
        return cache[n]

    if n <= 1:
        return n

    ergebnis = fib_schnell(n - 1) + fib_schnell(n - 2)

    # save the result before returning it, this is the important part
    cache[n] = ergebnis
    return ergebnis


if __name__ == "__main__":
    zahl = int(input("die wievielte fibonacci zahl willst du wissen? "))

    start = time.time()
    ergebnis_schnell = fib_schnell(zahl)
    dauer_schnell = time.time() - start
    print(f"schnelle version: {ergebnis_schnell} (dauer: {dauer_schnell:.6f} sekunden)")

    # nur die langsame version testen wenn die zahl nicht zu gross ist
    # sonst wartet man ewig, hab das am eigenen leib erfahren mit n=40
    if zahl <= 30:
        start = time.time()
        ergebnis_langsam = fib_langsam(zahl)
        dauer_langsam = time.time() - start
        print(f"langsame version: {ergebnis_langsam} (dauer: {dauer_langsam:.6f} sekunden)")
    else:
        print("langsame version ueberspring ich, dauert bei so grossen zahlen ewig")

# crazy wie viel schneller die cache version ist, hab das erst nicht geglaubt
# bis ich beide nebeneinander getestet hab
