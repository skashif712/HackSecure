# Module 2 practice set (15 min each)


def digit_sum(n):
    total = 0
    for d in str(abs(n)):
        total += int(d)
    return total


# 6. Return the number whose digit sum is largest (ties go to the first).
def largest_digit_sum(nums):
    best = nums[0]
    for n in nums[1:]:
        if digit_sum(n) > digit_sum(best):   # ">" keeps the first on a tie
            best = n
    return best


# 7. Concatenate two arrays, remove duplicates keeping first occurrence order.
def merge_unique(a, b):
    result = []
    for x in a + b:
        if x not in result:
            result.append(x)
    return result


# 8. For each pair of adjacent words, True if the last letter of the first
#    equals the first letter of the second.
def word_chain(sentence):
    words = sentence.split()
    result = []
    for i in range(len(words) - 1):
        result.append(words[i][-1] == words[i + 1][0])
    return result


# 9. Reverse the digits of each number, keep the sign.
#    (Cut off in the photo, so this is my best read of it.)
def reverse_digits(nums):
    result = []
    for n in nums:
        reversed_n = int(str(abs(n))[::-1])   # int() drops leading zeros: 100 -> 1
        if n < 0:
            reversed_n = -reversed_n
        result.append(reversed_n)
    return result


if __name__ == "__main__":
    print(largest_digit_sum([19, 55, 302]))          # 19
    print(merge_unique([1, 2, 3], [2, 4, 1]))         # [1, 2, 3, 4]
    print(word_chain("apple egg grape"))              # [True, True]
    print(reverse_digits([123, -45, 100]))            # [321, -54, 1]

    assert largest_digit_sum([19, 55, 302]) == 19
    assert merge_unique([1, 2, 3], [2, 4, 1]) == [1, 2, 3, 4]
    assert word_chain("apple egg grape") == [True, True]
    assert word_chain("cat dog") == [False]
    assert reverse_digits([123, -45, 100]) == [321, -54, 1]
    print("All Module 2 tests passed")
