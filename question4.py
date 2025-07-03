#4. Write a Python program to compute the future value of a specified principal 
#amount, rate of interest, and number of years. (calculate simple interest based on 
#user input)

#Getting User Input
principal_amount = float(input("Enter the principal amount $: "))

interest_rate = float(input("Enter the interest rate %: "))

number_of_years = float(input("Enter the time in years: "))

#calculate the simple interest using PRT/100
simple_interest = (principal_amount * interest_rate * number_of_years) / 100

# Displaying the amount
print(f"The simple interest is: ${simple_interest}%")