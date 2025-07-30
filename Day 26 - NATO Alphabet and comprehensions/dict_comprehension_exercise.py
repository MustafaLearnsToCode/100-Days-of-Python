#dict comprehension - new_dict = {new_key:new_value for item in list}

#existing dictionary - new_dict ={new_key:new_value for (key,value) in dict.items()}

#Condiitonal dictionary comprehension - new_dict ={new_key:new_value for (key,value) in dict.tems() if test}

import random

#Generate random scores for students
names = ["Mustafa", "Alex", "Joseph", "Daniel", "Josh", "Kai"]
students_scores = {student:random.randint(0,100) for student in names}
print(students_scores)

#Creating dictionary with students who passed (score > 60)
passed_students ={student:score for (student,score) in students_scores.items() if score > 60}
print(passed_students)
