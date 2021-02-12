"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730246281"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    how_much: int = int(randint(1,4))
    if how_much == 1:
        return("Have a wonderful day")     
    else:
        if how_much == 2:
            return("You're mighty wise")
        else:
            if how_much == 3:
                return("The sun may rise based where you are")
            else:
                return("Your birthday comes once a year, don't forget")




# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
