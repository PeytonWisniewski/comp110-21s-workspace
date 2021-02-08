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
    print("A beautiful, smart, and loving person will be coming into you life.")       
else:
    if how_much == 2:
        print("Your life will be happy and peaceful.")
    else:
        if how_much == 3:
            print("Soon life will become more interesting.")
        else:
            print("When the sun is dark, you will experience brightness.")


print("Now, go spread positive vibes!")