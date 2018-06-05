# Instructions:

# Using a while loop, ask the user "How many numbers?", and then print out a chain of ascending numbers from 0 to the number input.

# After the results have printed, ask the user if they would like to continue. If "y" is entered, keep the chain running by inputting a new number and starting a new count from 0 to the number input. If "n" is entered, exit the application.

user_choice = input("How Many Numbers? ")

choose_continue = input("Continue the chain: (y)es or (n)o? ")

for x in range(2,20):
    while x < user_choice:
        print(x)
    else: 
        print('stop')

    if choose_continue == "y":
        print(x)
    else:
        print('done')
    
