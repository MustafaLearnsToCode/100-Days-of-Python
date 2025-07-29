# with open("weather_data.csv") as weather_data_file:
#     data = weather_data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data)) #dataframe
# print(type(data["temp"])) #series

#convert dataframe to dictionary
data_dict = data.to_dict()
print(data_dict)

#convert series to list
temp_list = data["temp"].to_list()
print(temp_list)

#temp average using python functions
print(sum(temp_list)/len(temp_list))

#temp average using .mean()
print(data["temp"].mean())

#temp mx using .max()
print(data["temp"].max())

#Get Data in columns
print(data["condition"]) #has to be perfect copy, make sure for capitalization
print(data.condition)

#Get Data in rows
print(data[data.day == "Monday"]) #first mention column, then row
print(data[data.temp == data.temp.max()]) #find row with max temp

#Find specific information in a row
monday = data[data.day == "Monday"]
print(monday.condition)

# converting monday's temp into Fahrenheit
temp_F = (monday.temp * 9/5) + 32
print(temp_F)

#Create Dataframe from scratch into csv file
data_dict = {
    "students": ["Mustafa", "Josh", "Joseph"],
    "scores": [100, 87, 73],
}
students_data = pandas.DataFrame(data_dict)
print(students_data)
students_data.to_csv("new_data.csv")