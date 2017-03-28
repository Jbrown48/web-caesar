import string

def alphabet_position(letter):
    alph = string.ascii_letters
    return (alph.find(letter) % 26)

def rotate_character(char, rot):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    if char in lower:
        newletter = lower[(alphabet_position(char) + rot) % 26]
        return(newletter)

    elif char in upper:
        newletter = upper[(alphabet_position(char) + rot) % 26]
        return(newletter)

    else:
        return(char)

def encrypt(text, rot):

    nexletter = ""
    newstring = ""

    for letter in text:
        nextletter = rotate_character(letter, rot)
        newstring += nextletter

    return(newstring)
