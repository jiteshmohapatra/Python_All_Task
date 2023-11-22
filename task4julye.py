a =int(input("enter a value in days"))
year = a/365
weeks = (a%365)/7
day = (a%365)%7 
print("The converted value in days to year is ",year)
print("The converted value in days to weeks is ",weeks)
print("The converted value in days  is ",day)