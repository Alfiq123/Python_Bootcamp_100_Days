# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# print("Welcome to rock paper scissors game!")
#
# rps = [rock, paper, scissors]
# computer_choice = random.randint(0, 2)
# # print(rps[rps_random])
#
# player_choice = int(input("What you choose: (0 for Rock, 1 for Paper, 2 for Scissors): "))
#
# # If Else for Player
# if player_choice == 0:
#     print(rock)
#     print("You choose Rock")
# elif player_choice == 1:
#     print(paper)
#     print("You choose Paper")
# elif player_choice == 2:
#     print(scissors)
#     print("You choose Scissors")
#
# # If Else For Computer
# if computer_choice == 0:
#     print(rock)
#     print("Computer choose Rock")
# elif computer_choice == 1:
#     print(paper)
#     print("Computer choose Paper")
# elif computer_choice == 2:
#     print(scissors)
#     print("Computer choose Scissors")
#
# if player_choice == 0 and computer_choice == 0:
#     print("\nDRAW")
# elif player_choice == 0 and computer_choice == 1:
#     print("\nCOMPUTER WINS - YOU LOSE")
# elif player_choice == 0 and computer_choice == 2:
#     print("\nYOU WIN - COMPUTER LOSE")
#
# if player_choice == 1 and computer_choice == 1:
#     print("\nDRAW")
# elif player_choice == 1 and computer_choice == 2:
#     print("\nComputer Win - You Lose")
# elif player_choice == 1 and computer_choice == 0:
#     print("\nYOU WIN - COMPUTER LOSE")
#
# if player_choice == 2 and computer_choice == 2:
#     print("\nDRAW")
# elif player_choice == 2 and computer_choice == 0:
#     print("\nComputer Win - You Lose")
# elif player_choice == 2 and computer_choice == 1:
#     print("\nYOU WIN - COMPUTER LOSE")

import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
