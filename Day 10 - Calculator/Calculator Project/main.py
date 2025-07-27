import art

print(art.logo)
print("Welcome to the calculator!")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1 = int(input("What is your first number?: "))
    game_over = True
    while game_over:
        for i in operations:
            print(i)
        operator = input("Pick an operation: ")
        num2 = int(input("What is your second number?: "))

        answer = operations[operator](n1 = num1, n2 = num2)
        print(f"{float(num1)} {operator} {float(num2)} = {float(answer)}")
        repeat = input(f"Type 'y' to continue calculating with {float(answer)} , or type 'n' to start a new calculation: ").lower()

        if repeat == "y":
            num1 = answer
        else:
            game_over = False
            print("\n" * 30)
            calculator()

calculator()

