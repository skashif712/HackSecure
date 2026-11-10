VOWELS = set("aeiouAEIOU")


def vowel_positions(s):
    """Return a list of 0-based indices where s has a vowel (a, e, i, o, u, any case)."""
    positions = []
    for i, ch in enumerate(s):
        if ch in VOWELS:
            positions.append(i)
    return positions


if __name__ == "__main__":
    print(vowel_positions("HackSecure"))  # [1, 5, 7, 9]
