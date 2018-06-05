# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = input("How many numbers? ")

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(int(user_number) + 1):

        # Print each number in the range
        print(x)

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")

    # Ask for how many numbers
# Print them out
# Ask again or quit

# if you get more numbers, add that many to the highest original number

playing = True
current_num = 1

while playing:
    number = input("How many numbers would you like or q to quit: ")
    if number != 'q':
        number = int(number)
        for x in range(current_num, current_num + number):
            print(x)
        current_num += number
    else:
        playing = False

# In 2 lists, we have dogs and their meals
# eg, Chance eats steak, lucky eats chow, etc...

dogs  = ['chance', 'scout', 'rover', 'lucky', 'boss']
meals = ['steak', 'chicken', 'bones', 'chow', 'vegan']

# If someone gives us a dog, how can we return their meal?

def find_meal(some_dog):
  pass
  #Return the meal the dog eats 
  # Hit, you'll have to use an index lookup and
  # Use that to find the meals
  #Rover --> Bones as an example

  # Ask for how many numbers
# Print them out
# Ask again or quit

# if you get more numbers, add that many to the highest original number

playing = True
current_num = 1

while playing:
    number = input("How many numbers would you like or q to quit: ")
    if number != 'q':
        number = int(number)
        for x in range(current_num, current_num + number):
            print(x)
        current_num += number
    else:
        playing = False


3 CommentsCollapse 

