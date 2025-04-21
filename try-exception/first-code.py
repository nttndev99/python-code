# ----------------------------------- 1
# try: 
#     file = open("a_file.txt") 
#     a_dictionary = {"key": "value"} 
#     print(a_dictionary["key"])
# except FileNotFoundError: # Nếu Try không tồn tại sẽ xảy ra FileNotFoundError
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message: # Nếu Try truy cập 1 key không tồn tại trong dict sẽ gây KeyError
#     print(f"The key {error_message} does not exist.")
# else: # Không lỗi 
#     content = file.read()
#     print(content)
# finally: # Dù lỗi hay không đều thực thi
#     file.close()
#     print("File was closed.")

# ----------------------------------- 2 - Raise Exception
# height = float(input("Height: "))
# weight = float(input("Weight: "))

# if height > 3: # Nếu sai phát sinh lỗi
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

# ----------------------------------- 3 - Index Error Handling
# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Frunt pie")
#     else:
#         print(fruit + " pie")

# make_pie(4) # Frunt pie
# make_pie(2) # Orange pie

# ----------------------------------- 4 - Key Error Handling
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass
    return total_likes