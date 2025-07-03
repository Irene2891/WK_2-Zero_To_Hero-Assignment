#3.Write a Python program to find the least common multiple (LCM) of two positive 
#integers. enter by the user from the terminal
import math
#To get the user input for the positive integers
integer1 = int(input("Enter a positive integer: "))

integer2 = int(input("Enter another positive integer: "))

# calculating the greatest common divisor (GCD) of the two integers

gcd_number = math.gcd(integer1, integer2)

#Calculating the least common mutiple(LCM) using the GCD

lcm_of_integers = int(integer1 * integer2)/ int(gcd_number)

print("The Least Common Multiple is:", lcm_of_integers)

