from sys import exit

def gold_room():
    print("It's a room full of gold! How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Please type a number.")

    if how_much < 50:
        print("Seems you're not very greedy. Or imaginative.")
        exit(0)
    else:
        dead("Tsk, tsk. Greed isn't good.")

def bear_room():
    print("""
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move this fat fuckin' bear?
    """)
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("Bad idea. The bear converts your face into something resembling cafeteria pizza.")
        elif choice == "taunt bear" and not bear_moved:
            print("""
            The bear has moved from the door.
            You can go through it now.
            """)
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("You just had to poke the bear.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I'm sorry, I don't understand.")

def cthulhu_room():
    print("""
    Here you see the great evil that is Cthulhu.
    The elder god stares deep into your eyes.
    Only madness awaits.
    You can try to flee, or eat your own head.
    What will it be?
    """)
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Fhtagn!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "You have died.")

def start():
    print("""
    You are in a dark room.
    There is a door to your right and a door to your left.
    Which do you take?
    """)

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("Apparently doors are too advanced for you. You stumble around until you are eaten by a grue.")

start()
