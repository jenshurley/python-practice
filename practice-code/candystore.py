# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]


# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)

print('welcome. you can choose 5 candies')

for i in range(allowance):
    candy_choice = input("Which candy would you like to bring home? ")
    print(type(candy_choice))
    candy_choice_idx = eval(candy_choice) #str converted to integer 
    candy_cart.append(candyList[candy_choice_idx])
                      #print the key value you are trying to manipulate
print(candy_cart)

print('cool. here is what ya got.')

for line_item in candy_cart:
    print(line_item)