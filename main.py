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
    min = 33
    max = 126

    if level == 1:
        min = 58
        max = 65
    
    if level == 2:
        min = 48
        max = 75

    for i in range(size):
        mdp += str(chr(randint(min, max)))
    return mdp

def defsize() -> int:
    size = input("Number of characters in the password : ")
    try:
        size = int(size)
    except ValueError:
        size = defsize()
    if size < 0:
        return defsize()
    return size

def deflevel() -> int:
    level = input("What level of difficulty : ")
    try:
        level = int(level)
    except ValueError:
        level = deflevel()
    if level <= 0:
        return deflevel()
    return level

if __name__ == "__main__":
    copy(mdp(defsize(), deflevel()))