#previous method
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

#using list comprehension - new_list = [new_item for item in list]
new_list = [n+1 for n in numbers]
print(new_list)

#you can also work with strings
name = "Angela"
new_list_name = [letter for letter in name]
print(new_list_name)

# Python sequences (lists, ranges, strings and tuples) - have a specific order and the list comprehension works like a for loop

#doubling the range
doubled_range = [2*n for n in range(1,5)]
print(doubled_range)

#conditional list comprehension - new_list = [new_item for item in list if test]
names = ["Mustafa", "Alex", "Joseph", "Daniel", "Josh", "Kai"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

#create a list with names longer than 5 letters in uppercase
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)
