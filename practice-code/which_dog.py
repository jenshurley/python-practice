dogs  = ['chance', 'scout', 'rover', 'lucky', 'boss']
meals = ['steak', 'chicken', 'bones', 'chow', 'vegan']
user_choice = input("which dog? ")

dog_meals = dict(zip(dogs,meals))

if user_choice in dog_meals:
    print(dog_meals[user_choice])
else:
    print ("not a valid dog")
