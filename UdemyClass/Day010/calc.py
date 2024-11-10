logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#create dictionary references
addnumbers = add
subnumbers = subtract
multnumbers = multiply
divnumbers = divide

calculations = {
    "+": addnumbers,
    "-": subnumbers,
    "*": multnumbers,
    "/": divnumbers
}

calc_cmd = "n"
operand1 = 0
operand2 = 0
operator = "n"
calculation = 0

print(logo)

while calc_cmd != "q":
    if calc_cmd != "y":
        operand1 = float(input("What's the first number?: "))
    
    
    for operands in calculations:
        print(f"{operands}\n")
    
    # only accept a valid operator
    while (operator in calculations) == False:
        operator = input("Pick an operation: ")
        
    operand2 = float(input("What's the next number?: "))
    
    if operator == "/" and operand2 == 0:
        print("ERROR: cannot divide by 0!\n")
    else:
        # perform calculations via dictionary lookup
        calculation = calculations[operator](operand1, operand2)
    
        print(f"{operand1} {operator} {operand2} = {calculation}")
    
    calc_cmd = (input(f"Type 'y' to continue calculating with {calculation}, type 'n' for start a new calculation, or 'q' to quit: ")).lower()
    
    operator = "n"
      
    if calc_cmd == 'y':
        operand1 = calculation
    
    
    
