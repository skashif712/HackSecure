def shift_letters(s):
    result = ""                 # start with an empty string

    for letter in s:            # go through the string one character at a time
        if letter == "z":       # z wraps around to a
            result += "a"
        elif letter == "Z":     # Z wraps around to A
            result += "A"
        elif "a" <= letter <= "y" or "A" <= letter <= "Y":   # any other letter
            result += chr(ord(letter) + 1)   # move one step forward: a -> b
        else:                   # not a letter (space, digit, !, ...)
            result += letter    # keep it as it is

    return result               # hand back the new string


# try it out
print(shift_letters("hello"))         # ifmmp
print(shift_letters("Zebra, zoo!"))   # Afcsb, app!
print(shift_letters("abc XYZ 123"))   # bcd YZA 123
