rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
img = [rock, paper, scissors]

print("Let's play rock, paper, scissors!")
ques = int(input("What do you choose? Type '0' for rock, '1' for paper and '2' for scissors:\n"))
if ques >= 0 and ques <= 2:
    print(img[ques])

computer = random.randint(0,2)
print(f"I chose:")
print(img[computer])

if ques >= 3 or ques < 0:
    print("Wrong input. You lose by default!")
elif computer == 2 and ques == 0:
    print("You win!")
elif computer == 0 and ques == 2:
    print("I win!")
elif computer > ques:
    print("I win!")
elif ques > computer:
    print("You win!")
elif computer == ques:
    print("It's a tie!")





