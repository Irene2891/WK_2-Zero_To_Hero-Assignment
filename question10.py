'''10 Write a Python program that reads two integers representing a month and 
day and prints the season for that month and day. 
 
    Expected Output: 
 
    Input the month (e.g. January, February etc.): july                      
    Input the day: 31                                                        
    Season is harmattan '''
#Solution
#get the user input for month and date
month = input("Enter the month: ")

day = int(input("Enter the day: "))

season  = "" 


if month.title() in ("December", "January", "February") and (1 <= day <= 31):

    season = "Winter"

elif month.title() in ("March","April", "May") and (day >= 1 and day <= 31):
    season = "Spring"

elif month.title() in  ("June","July","August") and (day >= 1 and day <= 31):
    season = "Summer"

elif month.title() in  ("September","October","November") and (day >= 1 and day <= 30):
    season = "Fall"

print(f"The season is {season} in {month}")

#else:
#print("Season not Known")