my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for item in my_list:
    counter = counter + item
    print(counter) # 1 3 6 10 15 21 28 36 45 55
print(counter) # 55


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in my_list:
    counter = 0
    counter = counter + item
    print(counter) # 1 2 3 4 5 6 7 8 9 10
print(counter) # 10