# Q. Create a script to filter only even numbers.
# We only care about even numbers, so we don't need an else block.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0

# iterating each number in list
for num in list1:
    # checking condition
    if num % 2 == 0:
        even_count += 1
        print("Even Number:", num)

print("Total even numbers:", even_count)
