"""
@author         catarme
@version        0.1
@since          28/06/2021
@param          Add the project on GitHub
"""

def mdp(size: int) -> str:
    mdp = str()
    for i in range(size):
        mdp += str(chr(randint(33, 126)))
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

if __name__ == "__main__":
    from random import randint
    from pyperclip import copy

    copy(mdp(defsize()))
    