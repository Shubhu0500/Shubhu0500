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

#Write your code below this line 👇0
import random

player_choice = int(input("what do you choose? 0 for rock, 1 for paper and 2 for scissors "))

if player_choice == 0:
  print(rock)
elif player_choice == 1:
  print(paper)
else:
  print(scissors)


computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")

if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)

if player_choice == 0 and computer_choice == 2:
  print("Congratulations!! You won")
elif computer_choice > player_choice:
  print("AHH! Hard luck You lose")
elif computer_choice == player_choice:
  print("OHHH! It's a draw")
else:
  print("Invalid Choice, Game Over!!")

print("Hope you enjoyed the game!")

