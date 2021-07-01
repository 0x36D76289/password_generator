"""
@author         catarme
@version        0.2
@since          28/06/2021
@param          Added the possibility to choose a password difficulty level.
"""
from random import randint
from pyperclip import copy

def mdp(size: int, level: int) -> str:
    mdp = str()
    min, max = 33, 126

    if level == 1:
        min, max = 58, 65
    
    if level == 2:
        min, max = 48, 75

    for i in range(size):
        mdp += str(chr(randint(min, max)))
    return mdp

def defsize() -> int:
    try:
        number = int(input("Number of characters in the password : "))
        if number <= 0:
            raise ValueError
    except ValueError:
        return defsize()
    return number

def deflevel() -> int:
    try:
        number = int(input("What level of difficulty : "))
        if number < 0:
            raise ValueError
    except ValueError:
        return defsize()
    return number

if __name__ == "__main__":
    copy(mdp(defsize(), deflevel()))