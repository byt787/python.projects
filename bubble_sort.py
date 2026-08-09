# bubble sort, probably the simplest sorting algorithm to learn
# not fast or anything but at least you understand WHY it works

zahlen = [5, 2, 9, 1, 5, 6, 3, 8]

print("vorher:", zahlen)

n = len(zahlen)

# outer loop, once per pass
for durchgang in range(n):
    # inner loop always compares 2 neighbors and swaps them if theyre in the wrong order
    # the -durchgang -1 part is because the biggest numbers already "bubbled" to the end
    # and dont need to be checked again (i think thats also why its called bubble sort)
    for i in range(0, n - durchgang - 1):
        if zahlen[i] > zahlen[i + 1]:
            # classic swap, at first i thought youd need a 3rd variable for this
            # but python can do it without one
            zahlen[i], zahlen[i + 1] = zahlen[i + 1], zahlen[i]

print("nachher:", zahlen)

