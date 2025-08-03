with open("a_file.txt") as file:
    file.read()

#KeyError
dictionary = {"key":"value"}
value = dictionary["non_existent_key"]

#InexError
fruit_list = ["apple", "banana", "orange"]
fruit = fruit_list[3]

#TypeError
text = "abc"
print(text + 5)

#try: something that might cause an exception
#except: Do this if there was an exception - something went wrong
#else: do this when there were no exceptions
#finally: do it no matter what happens - usually used for cleaning things up

#FileNotFound
try:
    file = open("a_file.text")
    dictionary = {"key":"value"} #exception is too broad - so it catches all errors
    print(dictionary["adqwef"])
except FileNotFoundError: #You can define specific errors
    file = open("a_file.text", "w")
    file.write("something")
except KeyError as error_message: #sepcify where the error is using 'as'
    print(f"That key {error_message} not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over three meters")

bmi = weight/height ** 2
print(bmi)
