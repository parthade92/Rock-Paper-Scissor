import random as r
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
choice = [rock, paper, scissors]
c = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp = r.randint(0, 2)
print(f"Your Choice:\n{choice[c]}")
print(f"Computer's Choice:\n{choice[comp]}")
if c == comp:
    print("It's a Draw")
elif c == 2 and comp == 1:
    print("You Win")
elif c == 1 and comp == 0:
    print("You Win")
elif c == 0 and comp == 2:
    print("You Win")
else:
    print("You Lose")
