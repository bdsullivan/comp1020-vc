#This foo module contains all necessary functions for our demo
#Blair D. Sullivan

def whiz_bang(whiz, bang):
    if whiz:
        print("Whiz")
    if bang:
        print("Bang")


def beep_boop(beeps: int, booper: int) -> None:

    for i in range(beeps):
        if i % booper == 0:
            print("Boop!")
        else:
            print("Beep!")