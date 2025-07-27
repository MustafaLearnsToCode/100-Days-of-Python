#functions with outputs
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

format_name("MusTafA", "BADsHAh")

#created my own len function
def my_len(string):
    count_list = 0
    for i in string:
        count_list += 1
    return count_list

number = my_len("Hello")
print(number)

#using return
def function_1(text):
    return text + text
def function_2(text):
    return text.upper()

output = function_2(function_1("hello"))
print(output)