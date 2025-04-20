numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

name = "This is a name"
letter_list = [letter for letter in name]
# print(letter_list)

range_list = [num * 2 for num in range(1, 4)] # <=> range(1, 2, 3)
# print(range_list)

names = ["Alex", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)
# print(long_names)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings ] # convert int numbers
result = [n  for n in numbers if n % 2 == 0 ] # even numbers
# print(result)


# Read lines from both files and convert them to sets of integers
with open("./comprehensions/lists-comprehension/file1.txt") as file1:
    file1_numbers = [int(line.strip()) for line in file1.readlines()]
with open("./comprehensions/lists-comprehension/file2.txt") as file2:
    file2_numbers = [int(line.strip()) for line in file2.readlines()]
# Find common numbers using list comprehension
result = [num for num in file1_numbers if num in file2_numbers]
print(result)