print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 15 20 25 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip/100 * bill + bill
bill_person = bill_with_tip/people
final_amount = round(bill_person, 2)
final2 = round(bill_with_tip, 2)
print(f"Your total bill is {bill_with_tip} dollars")
print(f"Your bill per person should be: {final_amount} dollars")


