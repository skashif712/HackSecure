def get_vowels(s):
    vowels = "aeiouAEIOU"   # the letters we care about
    found = []              # empty list to store the vowels we find

    for letter in s:            # go through the string one letter at a time
        if letter in vowels:    # is it a vowel?
            found.append(letter) # yes, so save the letter

    return found                # hand back the list


# try it out
print(get_vowels("hello"))       # ['e', 'o']
print(get_vowels("HackSecure"))  # ['a', 'e', 'u', 'e']
