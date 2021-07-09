"""
@author         catarme
@version        0.4
@since          10/07/2021
@param          Copies the password to the Windows clipboard.
"""
from random import randint
from pyperclip import copy

def generatepassword(size: int, level: int) -> str:
    """
    Generates a "size" character password.
    """
    password = str()
    for i in range(size):
        password += chr(randint(33, 126))
    return password

def defsize() -> int:
    """
    Checks that the variable entered is usable.
    """
    try:
        number = int(input("Number of characters in the password : "))
        if number <= 0:
            raise ValueError
    except ValueError:
        return defsize()
    return number

def deflevel() -> int:
    """
    Checks that the variable entered is usable.
    """
    try:
        number = int(input("What level of difficulty : "))
        if number < 0:
            raise ValueError
    except ValueError:
        return defsize()
    return number

if __name__ == "__main__":
    copy(generatepassword(defsize(), deflevel()))
