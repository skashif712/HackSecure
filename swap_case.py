def swap_case(input_string):
    result = ""                 # start with an empty string

    for letter in input_string:     # go through one character at a time
        if "a" <= letter <= "z":    # lowercase letter?
            result += chr(ord(letter) - 32)   # make it uppercase: a -> A
        elif "A" <= letter <= "Z":  # uppercase letter?
            result += chr(ord(letter) + 32)   # make it lowercase: A -> a
        else:                       # not a letter (space, digit, !, ...)
            result += letter        # keep it as it is

    return result                   # hand back the new string


# try it out
print(swap_case("Hello World"))     # hELLO wORLD
print(swap_case("HackSecure 2026!"))  # hACKsECURE 2026!
