#13. Write a program that takes three numbers as input and prints the largest one 
#using if-elif-else. 

num1 = int(input("1. Input a number: "))
num2 = int(input("2. Input a number: "))
num3 = int(input("3. Input a number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")