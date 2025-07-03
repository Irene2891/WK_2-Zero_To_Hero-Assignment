'''8.Write a Python program to check the validity of passwords input by users. 
Validation : 
At least 1 letter between [a-z] and 1 letter between [A-Z]. 
    At least 1 number between [0-9]. 
    At least 1 character from [$#@]. 
    Minimum length 6 characters. 
    Maximum length 16 characters.'''

import re # importing the module that contains the search functionality(re:regular expression)

#getting the user password
user_password = input("Enter Your Password: ")

user_password_length = len(user_password)

is_valid = False

# checking if the password inputted by the user meets the stated conditions
# using the while loop

while True:
    if user_password_length < 6 or user_password_length > 20:  # to check for password character length
          break
    elif not re.search('[A-Z]', user_password): # to check for capital letters
          break 
    elif not re.search('[a-z]', user_password): # to check for small letters
          break 
    elif not re.search('[0-9]', user_password): # to check for numbers between 0-9
          break 
    elif not re.search('[$#@]', user_password): # to check for special characters
          break 
    elif  re.search('\s', user_password): # to remove whitespaces
          break 
    else:
        is_valid = True
        break
if is_valid: #if all conditions are met
        print("Password is good")
else:
        print("Password is invalid. Check Your Password and try again")

    


#if len(user_password) < 6 or len(user_password) > 16
