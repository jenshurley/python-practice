# items = ["write", "code", "sleep"]
# #lists let you iterate over them

# for x in items:
#     print(x, "is the item you are iterating over")
#     break
#     #this will only print  the first item


#Rock Paper Scissor Game
# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == computer_choice:
   print("you tied")
elif user_choice == "r" and computer_choice == "s":
   print ("you win")
elif user_choice == "r" and computer_choice == "p":
   print("you loose")
elif user_choice == "s" and computer_choice == "r":
   print ("you loose")
elif user_choice == "p" and computer_choice == "r":
   print ("you win")
else:
   print("you loose")

import random

choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

user_choice = input("select Rock, Paper or Scissors: ")
cpu_choice = choices[random.choice(list(choices.keys()))]
print(cpu_choice)

if user_choice == cpu_choice:
    print('tie!')

lookup_choice = (user_choice, cpu_choice)

results = {('Paper','Rock') : True,
            ('Paper','Scissors') : False,
            ('Rock','Paper') : False,
            ('Rock','Scissors') : True,
            ('Scissors','Paper') : True,
            ('Scissors','Rock') : False}

if results[lookup_choice]:
    print('You Win!')
else:
    print('You Lose')