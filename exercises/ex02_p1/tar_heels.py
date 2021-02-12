"""Tar Heels exercise redux as a structured program."""

__author__ = "730246281"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(g: int) -> str:
    a: int = g
    b: int = a % 2
    c: int = a % 7
    d: bool = b == 0 and c == 0
    e: bool = b == 0
    f: bool = c == 0

    if d is True: 
        return("TAR HEELS")
    else:
        if f is True:
            return("HEELS")
        else:
            if e is True:
                    return("TAR")
            else:
                return("CAROLINA")

if __name__ == "__main__":
    main()
