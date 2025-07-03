#Write a Python program to calculate the hypotenuse of a right angled triangle.
import math #importing the math library
# getting the user input
right_side = float(input("Enter the value of the right side: "))

base_side = float(input("Enter the value of the base: "))
# calculating the hypotenus using 

hypotenus = math.sqrt(right_side **2 + base_side **2)

print("The hypotenus of the right angled triangle is: ", hypotenus)