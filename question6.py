'''6. Write a Python program to convert height (in feet and inches) to centimeters.
1 foot = 12 inches
1 inch = 2.54 cm'''

inches = float(input("Enter your height in inches: "))

foot = float(input("Enter your height in feet: "))

#calculating from feet to centimeters
feet_cm = foot * 12 * 2.54

inches_cm = inches * 2.54

cm = feet_cm + inches_cm
# Displaying the result
print("Your Height in Centimeters is: ", cm)