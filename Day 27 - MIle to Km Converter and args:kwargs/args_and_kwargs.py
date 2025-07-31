#functions can be set with default values - they only change when you specify it when calling the function
"""def functions(a=1, b=2, c=3)
   do this with a
   do this with b
   do this with c
function(b=4)"""

# *args - used for multiple arguments (the asterisk is important - you can name it anything else)

#create function to add an unlimited number of arguments
def add(*args):
    #They act as tuples
    print(args[0])
    #that's why they are known as unlimited positional arguments
    total = 0
    for n in args:
        total += n
    return total

print(add(1,2,3))

#**kwargs are multiple keyword arguments - they create a dictionary of arguments
def calculate(n, **kwargs):
    print(kwargs)
    """for key,value in kwargs.items():
        print(key)
        print(value)"""

    print(kwargs['add'])

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2,add=3, multiply=5)

#Implementing kwargs into class attributes initialization
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model") #.get() can be used instead of square brackets but when there is no value it just returns None
        self.color = kwargs.get("color")
        self.color = kwargs.get("seats")

my_car = Car(make="Porsche", model="911", color="black")
print(my_car)