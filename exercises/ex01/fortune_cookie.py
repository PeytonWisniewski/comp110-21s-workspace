"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730246281"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

how_much: int = int(randint(1, 4))

print("Your fortune cookie says...")

if how_much == 1:
        print("You have great wisdom, use it wisely.")       
else:
    if how_much == 2:
            print("Your true love is closer than you think.")
    else:
        if how_much == 3:
                print("Comp will always be here for you.")
        else:
                print("When the sun is dark, you will experience brightness.")


print("Now, go spread postivie vibes!")