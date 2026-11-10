# Module 1 practice set (10 min each)


# 1. Count numbers divisible by 3 but not by 5.
def count_div3_not5(nums):
    count = 0
    for n in nums:
        if n % 3 == 0 and n % 5 != 0:
            count += 1
    return count


# 2. Uppercase every second character (index 1, 3, 5...).
def upper_every_second(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 1:
            result += s[i].upper()
        else:
            result += s[i]
    return result


# 3. Longest word in a sentence (first one if tied).
def longest_word(sentence):
    longest = ""
    for word in sentence.split():
        if len(word) > len(longest):   # ">" not ">=" keeps the first on a tie
            longest = word
    return longest


# 4. Difference between max and min of an array.
def max_min_diff(nums):
    if not nums:
        return 0
    return max(nums) - min(nums)


# 5. Count words that start and end with the same letter.
def same_start_end(sentence):
    count = 0
    for word in sentence.split():
        if word[0] == word[-1]:
            count += 1
    return count


if __name__ == "__main__":
    print(count_div3_not5([3, 15, 9, 10]))         # 2
    print(upper_every_second("abcdef"))             # aBcDeF
    print(longest_word("I love python"))            # python
    print(max_min_diff([4, 9, 1, 7]))               # 8
    print(same_start_end("level noon cat dad"))     # 3

    assert count_div3_not5([3, 15, 9, 10]) == 2
    assert upper_every_second("abcdef") == "aBcDeF"
    assert longest_word("I love python") == "python"
    assert longest_word("cat dog") == "cat"
    assert max_min_diff([4, 9, 1, 7]) == 8
    assert max_min_diff([]) == 0
    assert same_start_end("level noon cat dad") == 3
    print("All Module 1 tests passed")
