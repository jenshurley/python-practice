# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")


while shopping == "y":
    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")
    pie_choice = input("Pick the pie number you'd like ")
    pie_purchases[int(pie_choice)-1] +=1 
    print("Great! You've picked the pie " + pie_list[int(pie_choice)-1])         
    shopping = input("Pie? y or n ")

print("Time to checkout. Here's your order")

pie_orders = (list(zip(pie_purchases, pie_list)))

for pie in pie_orders:
   print("You ordered", pie)

##END OF SOLUTION
#everytime you loop through, ask for another set of input

# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases, how could we have made this dynamically?
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#you need a data structure to keep track of the number of pies of a certain type

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")



while shopping == "y":
#while loop bc we don't know when to quit
    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")    
    
    selection = input("Pick the pie number you'd like: ")
    pie_name = pie_list[eval(selection) - 1] #you have to convert str to int
    pie_purchases[eval(selection) - 1] += 1 # Increment pie count
    print("Great, you have picked the pie {}".format(pie_name))
    #curly brackets - placeholder getting filled by format method on string which accepts variable pie_name. this is how you write it in professional python/
    

    next_step  = input("Would you like to add another pie? (y) or checkout (n)")
    
    if next_step == 'n':
        print("Time to checkout, heres your order")
        for x in range(len(pie_purchases)):
            print("You ordered {} of  {} ".format(pie_purchases[x], pie_list[x])   )
        shopping = False

# mention enumerate
# Dictionary would have been a more logical choice