# #This is a comment

# print('hi')

# name = "Jen"

# print(name)

# #Variables not encased in string unless you ""

# age = 108
# print(age + 99)

# longstring = "Hi this is a long string that we want to output"

# print (name +" " + longstring)

# print("Hi my name is ", name, "and I am", age, " years old")

# #boolean value - evaluates t/f

# happy = True

# if happy: 
#     print("happy, yes.")
    

name = input("Hi, what is your name? ")

if name == "Jen":
    print(name)
else:
    print("you can't use this program")

age = input("How old are you? ")

if age == "100":
    print("wow, " + age)
else: 
    print("um, are you sure? ")

true = input("Is this statement true? ")

# if true == "Yes":
#     print("ok")
# else:
#     print("hmm")

    
if true in ['t', 'yes', 'Yes']:
      print("ok")
else:
    print("no. just no")
    