import pandas

# Dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Loop through dictionaries:
for (key, value) in student_dict.items():
    print()

# Data frame
student_data_frame = pandas.DataFrame(student_dict)
print()

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print()

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    if row.student == "James":
        print(row.score)

