principal_amount = int(input("Please enter the principal amount: "))
timePeriod = int(input("Please enter the time period in months: "))
rateOfInterest = int(input("Please enter the Rate of interest: "))

simpleInterest = ((principal_amount*timePeriod*rateOfInterest)/100)

print("Your simple interest is: ", simpleInterest)