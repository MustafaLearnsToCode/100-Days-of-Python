student_dict = {
    "students": ["Mustafa", "Daniel", "Josh"],
    "scores": [100,23,98]
}

#looping through dictionaries
for (key,value) in student_dict.items():
    print(value)

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

#looping through a dataframe
for (key,value) in student_dataframe.items():
    print(value)

#looping through rows of dataframe
for (index, row) in student_dataframe.iterrows():
    if row.students == "Mustafa":
        print(row.scores)