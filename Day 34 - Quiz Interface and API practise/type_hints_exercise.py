age: int
name: str
height: float
is_human: bool

#specify data type to reduce errors in the future.
def police_check(age: int) -> bool: #a type hint (->) is used to decide the output for the function
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(12))

#can you in if statements
if police_check(19):
    print("You may pass")
else:
    print("Pay the fine")

age = "12"