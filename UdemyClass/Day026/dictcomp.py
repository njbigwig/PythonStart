import random
import pandas

# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key,value) in dict.items()}
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}


# goal is create a dictionary:
# student_score = {
#  "Alex": 89,
# "Beth": 98  
#}
names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: random.randint(50,100) for student in names_list}
print(f"Class Scores: {student_scores}")

passed_students = {students[0]: students[1] for students in student_scores.items() if students[1] >= 60}
print(f"Passing Scores #1: {passed_students}")

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(f"Passing Scores #2: {passed_students}")

# Interate over Pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

print("\n")

for (key, value) in student_dict.items():
    print(f"{key} {value}")
    
print("\n")
    
# can loop through a Pandas DataFrame
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

print("\n")

for (key, value) in student_data_frame.items():
    print(f"{value}")
    
print("\n")

# built in Panda to loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #print(index)
    print(row.student) # Pandas series object - shows just the names
    print(row.score) # Pandas series object - shows just the scores
    
    
    
