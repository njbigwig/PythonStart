print("Ticket Box\n\n")
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5")
        bill = 5
    elif age >= 12 and age <= 18:
        print("Youth tickets are $7")
        bill = 7
    elif age > 18 and age <= 44:
        print("Adult tickets are $12")
        bill = 12
    else:
        print("Senior tickets are $0")
        bill = 0

    wants_photo = input("Do you want a phone (y = Yes/n = No)? ")
    if wants_photo == "y":
        bill = bill + 3
    print(f"You bill = ${bill}")
else:
    print("Sorry :( You have to be taller to ride the rollercoaster")