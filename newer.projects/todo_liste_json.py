# to-do list that actually saves stuff to a file, so it doesnt just
# disappear every time i close the terminal like my other scripts did

import json
import os

DATEI_NAME = "todos.json"


def todos_laden():
    # if the file doesnt exist yet (first time running this) just start
    # with an empty list instead of crashing
    if not os.path.exists(DATEI_NAME):
        return []

    with open(DATEI_NAME, "r") as datei:
        return json.load(datei)


def todos_speichern(todos):
    with open(DATEI_NAME, "w") as datei:
        # indent=2 just makes the json file readable if you open it manually
        json.dump(todos, datei, indent=2)


def todo_hinzufuegen(todos, text):
    # every todo is a little dict, easier to extend later (deadline, tags etc)
    # than if i just used plain strings
    neues_todo = {"text": text, "erledigt": False}
    todos.append(neues_todo)
    print(f"hinzugefuegt: {text}")


def todo_erledigen(todos, index):
    # index - 1 because i show the list starting at 1, feels more natural
    # for a user than starting at 0
    if 0 <= index - 1 < len(todos):
        todos[index - 1]["erledigt"] = True
        print("als erledigt markiert")
    else:
        print("gibts nicht, check die nummer nochmal")


def todos_anzeigen(todos):
    if not todos:
        print("keine todos vorhanden, entweder fleissig oder faul :)")
        return

    for i, todo in enumerate(todos, start=1):
        haken = "[x]" if todo["erledigt"] else "[ ]"
        print(f"{i}. {haken} {todo['text']}")


def menu_anzeigen():
    print("\nwas willst du tun?")
    print("1 - todo hinzufuegen")
    print("2 - todo erledigen")
    print("3 - alle todos anzeigen")
    print("4 - beenden")


if __name__ == "__main__":
    todos = todos_laden()

    # while true mit break ist glaub der einfachste weg fuer sowas ein menu
    while True:
        menu_anzeigen()
        auswahl = input("> ")

        if auswahl == "1":
            text = input("was steht an? ")
            todo_hinzufuegen(todos, text)
            todos_speichern(todos)
        elif auswahl == "2":
            todos_anzeigen(todos)
            nummer = int(input("welche nummer ist erledigt? "))
            todo_erledigen(todos, nummer)
            todos_speichern(todos)
        elif auswahl == "3":
            todos_anzeigen(todos)
        elif auswahl == "4":
            print("bis dann")
            break
        else:
            print("kenn ich nicht, nimm 1-4")

# note to self: die datei landet im gleichen ordner wo das script laeuft
# falls ich das mal irgendwo anders speichern will muss ich den pfad anpassen
