def whiz_bang(whiz: bool = True, bang: bool = False) -> None:

    if whiz:
        print("Whiz")
    elif bang:
        print("Bang")


def beep_boop(beeps: int, booper: int) -> None:

    for i in range(beeps):
        if i % booper == 0:
            print("Boop!")
        else:
            print("Beep!")