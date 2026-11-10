# Practice 5: Given an array, return how many elements equal the sum of
# their two neighbors. Skip the first and last elements.
# Watch out for: empty input, single-element arrays, off-by-one in range.


def solution(arr):
    count = 0
    # range(1, len(arr) - 1) skips the first and last elements.
    # For empty or 1-2 element arrays this range is empty, so we return 0.
    for i in range(1, len(arr) - 1):
        if arr[i] == arr[i - 1] + arr[i + 1]:
            count += 1
    return count


# Tests
print(solution([1, 3, 2, 5, 3]))   # 3 = 1+2, 5 = 2+3 -> 2
print(solution([0, 0, 0]))         # 0 = 0+0 -> 1
print(solution([4, 1, 2]))         # 1 != 4+2 -> 0
print(solution([]))                # empty -> 0
print(solution([7]))               # single element -> 0
print(solution([7, 8]))            # no middle elements -> 0
