import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

print("Easy + hard approaches - add random letters, symbols, then numbers in series AND then randomize the string!")

passwordstring = ""
shufflepasswordstring = ""


for pwdidx in range(0, nr_letters):
    passwordstring += random.choice(letters)

for pwdidx in range(0, nr_symbols):
    passwordstring += random.choice(symbols)   
    
for pwdidx in range(0, nr_numbers):
    passwordstring += random.choice(numbers)
    
print(f"Your straight password = {passwordstring} len = {len(passwordstring)}")

# this will create a scrambled list[]
shufflepasswordlist = random.sample(passwordstring, len(passwordstring))

# convert list to a string
for pwdchar in shufflepasswordlist:
    shufflepasswordstring += pwdchar
    
print(f"Your scrambled password = {shufflepasswordstring} len = {len(shufflepasswordstring)}")

    

    
