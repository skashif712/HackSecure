def vowel_positions(s):
    vowels = "aeiouAEIOU"   # the letters we care about
    positions = []          # empty list to store the answers

    for i in range(len(s)):     # go through every position: 0, 1, 2, ...
        letter = s[i]           # grab the letter at that position
        if letter in vowels:    # is it a vowel?
            positions.append(i) # yes, so save its position

    return positions            # hand back the list


# try it out
print(vowel_positions("hello"))       # [1, 4]
print(vowel_positions("HackSecure"))  # [1, 5, 7, 9]
