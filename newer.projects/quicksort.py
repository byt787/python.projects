# quicksort, next level after bubble sort. this one uses recursion which
# broke my brain a little at first but makes sense now i think

def quicksort(liste):
    # base case: a list with 0 or 1 elements is already sorted, nothing to do
    if len(liste) <= 1:
        return liste

    # picking the middle element as the pivot, could also take the first
    # or last one but middle seemed like a decent choice from what i read
    pivot = liste[len(liste) // 2]

    # splitting everything into 3 groups compared to the pivot
    kleiner = [x for x in liste if x < pivot]
    gleich = [x for x in liste if x == pivot]
    groesser = [x for x in liste if x > pivot]

    # this is the recursive part, sort the smaller and bigger groups
    # again and again until everything is just single elements
    return quicksort(kleiner) + gleich + quicksort(groesser)


if __name__ == "__main__":
    zahlen = [8, 3, 9, 1, 7, 2, 5, 4, 6, 0]
    print("vorher:", zahlen)

    sortiert = quicksort(zahlen)
    print("nachher:", sortiert)

    # kleiner extra test mit ner liste die schon sortiert ist, wollte checken
    # ob das ding dann trotzdem richtig durchlaeuft
    schon_sortiert = [1, 2, 3, 4, 5]
    print("war schon sortiert:", quicksort(schon_sortiert))

# note to self: das mit list comprehensions 3x durch die liste zu gehen ist
# nicht die schnellste loesung aber am einfachsten zu verstehen fuer mich grad
# gibt bestimmt ne in-place version die weniger speicher braucht, muss ich mal googeln
