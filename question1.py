'''1. Write a Python program that calculates the area of a circle based on the radius
entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504'''

#Solution
#To get the User Input for Radius

radius =float(input("Enter the radius of a circle: "))

print(f"The radius of the circle is r = {radius}")

# Calculating the area using the formula: a = pi* radius^2

pi = 22 /7

area = pi * (radius ** 2)

print(f"Area  is {area}")


