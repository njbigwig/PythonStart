print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

pizzacost = 0

if size == "s":
    pizzacost = 15
elif size == "m":
    pizzacost = 20
else:
    pizzacost = 25

if pepperoni == "y":
    if size == "s":
        pizzacost += 2
    else:
        pizzacost += 3

if extra_cheese == "y":
    pizzacost += 1

print(f"Your final bill: ${pizzacost}.")
