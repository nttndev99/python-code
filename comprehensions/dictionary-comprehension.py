names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

import random
students_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(students_scores)
# print(passed_students)

# Split and len word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)




