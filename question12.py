'''12. A shop offers a 10% discount if the total bill is over $100. Write a program 
that asks for the total bill amount and prints the final amount to be paid after the 
discount, if applicable. '''

total_bill = int(input("What is your total bill of items purchased: "))

if total_bill > 100:
    Discount_price= total_bill * 10/100
    final_amount= total_bill - Discount_price
    print(f"Your amount after discount is ${final_amount:.2f}")
else:
    print("Your Purchase is below $100, hence you do not have a discount") 

    