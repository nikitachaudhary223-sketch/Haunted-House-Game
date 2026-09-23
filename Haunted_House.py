print("************************")
print("ESCAPE THE HAUNTED HOUSE")
print("************************")

player={
    "name":"",
    "health":100,
    "key":False,
    "clue":"False"
}

player["name"]=input("Enter your name:")

print("You wake up inside a dark, abandoned house....")
print("The door behind you is locked.")
print("You must find a way to escape!")

def show_status():
    print("-------STATUS------")
    print("Name:",player["name"])
    print("Health:", player["health"])
    print("Key:", player["key"])
    print("Clue:", player["clue"])
    print("----------------------------")

def kitchen():
    print("You enter the kitchen.")
    print("There is an old table and a storage cupboard.")

    choice=input("Do you search the cupboard? (yes/no)").lower()

    if choice=="yes":
        print("You found a mysterious clue!")
        player["clue"]="True"

    else:
        print("You leave the kitchen.")

def bedroom():
    print("You enter the bedroom.")
    print("Suddenly,something moves under the bed!")

    choice=input("Do you look under the bed? (yes/no): ").lower()

    if choice=="yes":
        print("A ghost appears!")
        player["health"] -= 30
        print("You lost 30 health!")

        if player["health"] > 0:
            print("You escape from the room.")
    else:
        print("You carefully leave the bedroom.")

def basement():
    print("You enter the dark basement.")
    print("You see an old wooden box.")

    choice = input("Do you open the box? (yes/no): ").lower()

    if choice == "yes":
        print("You found the house key!")
        player["key"] = True
    else:
        print("You decide not to open the box.")

def escape():
    print("You find the main door.")

    if player["key"] and player["clue"]:
        print("You use the key to unlock the door.")
        print("The clue helped you discover the secret escape route.")
        print("CONGRATULATIONS!")
        print("You escaped the haunted house!")
        return True

    elif player["key"]:
        print("You have the key, but the door has a strange lock.")
        print("You need to find a clue first.")
        return False

    else:
        print("The door is locked.")
        print("You need to find a key.")
        return False

while player["health"] > 0:

    show_status()

    print("\nWhere do you want to go?")
    print("1. Kitchen")
    print("2. Bedroom")
    print("3. Basement")
    print("4. Try to escape")

    choice = input("Enter your choice: ")

    if choice == "1":
        kitchen()

    elif choice == "2":
        bedroom()

    elif choice == "3":
        basement()

    elif choice == "4":
        if escape():
            break

    else:
        print("Invalid choice!")

    if player["health"] <= 0:
        print("Your health reached 0.")
        print("You couldn't escape the haunted house.")

print("==============================")
print("        GAME OVER")
print("==============================")

