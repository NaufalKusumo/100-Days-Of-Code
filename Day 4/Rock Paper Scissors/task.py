import random


def calculateFight(user, computer):
    if user == computer:
        print("It's a draw!")
    elif (user - computer) % 3 == 1:
        print("You win!")
    else:
        print("Computer wins!")


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

# List of choices
tools = [rock, paper, scissors]

print("Choose rock (0), paper (1), or scissors (2):")
userChoice = int(input())

if userChoice not in [0, 1, 2]:
    print("Invalid choice! Please select 0, 1, or 2.")
else:
    print(f"You chose:\n{tools[userChoice]}")

    compChoice = random.randint(0, 2)
    print(f"Computer chose:\n{tools[compChoice]}")

    calculateFight(userChoice, compChoice)
