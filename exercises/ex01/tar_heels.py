"""An exercise in remainders and boolean logic."""

__author__ = "730246281"


# Begin your solution here...
a: int = int(input("Enter an int: "))
b: int = a % 2
c: int = a % 7
d: bool = b == 0 and c == 0
e: bool = b == 0
f: bool = c == 0

if d is True: 
    print("TAR HEELS")
else:
    if f is True:
        print("HEELS")
    else:
        if e is True:
            print("TAR")
        else:
            print("CAROLINA")