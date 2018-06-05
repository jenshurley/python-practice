
# # First we'll import the os module
# # This will allow us to create file paths across operating systems
# import os
# # Module for reading CSV's
# import csv
# csvpath = os.path.join('..', 'databootcamp', 'netflix.csv')
# print(csvpath)

# user_choice = input("which movie? ")

# # # Method 1: Plain Reading of CSVs
# # with open(csvpath, 'r') as file_handler:
# #     lines = file_handler.read()
# #     print(lines)
# #     print(type(lines))
# # Method 2: Improved Reading using CSV module

# with open(csvpath, newline='') as csvfile:
#     # CSV reader specifies delimiter and variable that holds contents
#     csvreader = csv.reader(csvfile, delimiter=',')
#     print(csvreader)
#     #  Each row is read as a row
#     found = None
#     for row in csvreader:
#         if row[0] == user_choice:
#             found = True
#             movie = row[0]
#             rating = row[1]
#             user_rating = row[6] 
#          #   print(movie, rating, user_rating)
#             print("{} is rated {} with a user rating of {}".format(movie,rating,user_rating))    
        
#             print("We're sorry. That movie cannot be found. Try again.")
#             found = False
#             break      
# # Add CommentCollapse  
# # Message Input

# # Message #class


import os

import csv

csvpath =   os.path.join('..', 'databootcamp', 'netflix.csv')

user_choice = input("What video are you looking for? ")
found = None

print(csvpath)


with open(csvpath, newline='') as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    for row in csvreader:
        if row[0] == user_choice:
            movie = row[0]
            rating = row[1]
            user_rating = row[6]
            print("{} is rated {} with a rating of {}".format(movie,rating,user_rating))
            found = True
            break
        
if found == None:
    print("not found")