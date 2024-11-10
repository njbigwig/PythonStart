# My tip calculator
print("Welcome to the tip calculator!\n")

bill = float(input("What was the total bill?: $"))

tip = float(input("How much tip would you like to give 10, 12, or 15?: "))/100.0

party = int(input("How many people to split the bill?: "))

payment = (bill * (1.0+tip))/party

print("Each person should pay: $" + str(round(payment,2)))




