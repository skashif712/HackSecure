def vowel_positions(s):
    vowels = "aeiouAEIOU"   # the letters we care about
    positions = []          # empty list to store the answers

    for i in range(len(s)):     # go through every position: 0, 1, 2, ...
        letter = s[i]           # grab the letter at that position
        if letter in vowels:    # is it a vowel?
            positions.append(i) # yes, so save its position

    return positions            # hand back the list


def show_vowels(s):
    positions = vowel_positions(s)   # get the vowel positions
    print("Word:", s)
    for i in positions:              # for each saved position...
        print("  position", i, "->", s[i])   # show the number and its letter
    print("  all positions:", positions)
    print()


# try it out
show_vowels("hello")
show_vowels("HackSecure")
