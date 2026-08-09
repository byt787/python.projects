# checks if a word or sentence is a palindrome
# meaning it reads the same forwards and backwards, like "anna" or "otto"

text = input("schreib ein wort oder nh satz :3:")

# lowercase everything first and remove spaces, otherwise "Anna" wouldnt count
# as a palindrome because the A is uppercase and the a at the end is lowercase
# didnt think of that at first xD and wondered why it didnt work 
bereinigt = text.lower()
bereinigt = bereinigt.replace(" ", "")

# [::-1] reverses the string and then we can compare the 2 strings by looking if
# theyre the same or not
umgedreht = bereinigt[::-1]

if bereinigt == umgedreht:
    print(text, "ist ein palindrom ^-^")
else:
    print(text, "ist leider kein palindrom :c")

# was fun to write this I did it at 4am or so with zero sleep but I think it turned out okay
