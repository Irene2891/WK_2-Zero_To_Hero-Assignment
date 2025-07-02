# 1. A program that simulates a login system with preset credentials(username and password)
#get the username
'''username = input("Please, enter Your Username: ").lower()

#get the password
password= input("Please, enter Your Password: ")
#Check for the conditions
if password == 1234 and username == "irenechichi":
    print("You've successfully logged into your account")
else:
    print("Your password or Username is Incorrect. Check and try again")'''

# 2. Ask the user for their name and favorite color

'''color = input("Please, tell us your favorite color: ")

name = input("Please, enter your name: ")

print(f"Hello {name}, your favourite color is {color}")'''

# 3. Prompt for a number. Print whether it's positive, negative and zero

'''number= float(input("Please, give us a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")'''

# 4. Write a program to calculate a customer's total bill based on:
#quantity,price. Print the result using f-string
'''item = input("Enter the name of the item: " )

quantity = int(input("Enter the quantity(ies) of item purchased: "))

price = float(input("Enter the Price of the item(s): \u20A6 "))

total = quantity * price

print(f"You purchased {quantity} pcs of {item}(s) at \u20A6{price:.2f} each.")
print(f"Your bill is {total:.2f}.\nThank you for shopping with us!🛒")'''

# 5. Prompt the user to enter their score

score = int(input("Enter your score between 0-100: "))

if 90 <= score <= 100:
    print("Your Grade is: A")
elif 80 <= score < 89:
    print("Your Grade is: B")
elif 70 <= score < 79:
    print("Your Grade is: C")
elif 0 <= score < 70:
    print("Your Grade is: F and you failed")
else:
    print("Your score is invalid. Please enter a value between 0 and 100.")
