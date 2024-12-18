cm_menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

cm_resources = {
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
}

cm_funds = 0.0

cm_icon = '☕'

def cm_show_menu():
    print("Coffee Machine Menu:")
    for choice in cm_menu:
        spaces = (10-len(choice))+3
        print(f"{choice} {' '*spaces}    ${cm_menu[choice]["cost"]:.2f}")
        
    print("\n")
        

def cm_report():
    global cm_funds
    
    print("\n\n")
    print("Current Resources:")
    for resource in cm_resources:
        print(f"{resource}:\t{cm_resources[resource][0]}{cm_resources[resource][1]}")
    print(f"Money: ${(cm_funds):.2f}")
    print("\n\n")

def cm_resource_check(cm_selection):
    cm_receipe = cm_menu[cm_selection]['ingredients']
    #print(cm_receipe)
    
    resource_check = True
    
    for ingredient in cm_receipe:
        #print(f"{ingredient} {cm_receipe[ingredient]}")
        
        if cm_receipe[ingredient] > cm_resources[ingredient][0]:
            print(f"   Sorry there is not enough {ingredient}")
            resource_check = False
        else:
            cm_resources[ingredient][0] -= cm_receipe[ingredient]            
    
    return resource_check

def cm_get_coins(cm_cost):
    global cm_funds
    print(f"Please deposit coins: ${(cm_cost):.2f}")
    
    correct_payment = True
    
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    
    payment = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    
    if payment < cm_cost:
        print(f"Sorry that's not enough money. ${(payment):.2f} refunded.")
        correct_payment = False
    elif payment > cm_cost:
        print(f"Here is ${(payment-cm_cost):.2f} in change.")
        cm_funds += cm_cost
    else:
        cm_funds += payment
        
    print("\n")
    
    return correct_payment
    
def cm_make_cup(cm_selection):
    #print(f"Selection = {cm_selection}")
    
    if cm_resource_check(cm_selection) == True:
        if cm_get_coins(cm_menu[cm_selection]["cost"]) == True:
            print("Preparing beverage...")
            print(f"Here is your {cm_selection}. Enjoy!")
            print(cm_icon)
            print("\n")
    else:
        print("Please chose another beverage...\n")



cm_cmd = "on"

while cm_cmd == "on":
    cm_show_menu()
    
    cm_cmd = input("What would you like? ").lower()
    print("\n")
    
    if cm_cmd == "off":
        print("Powering Down!")
    elif cm_cmd == "report":
        cm_report()
        cm_cmd = "on"
    elif cm_cmd == "espresso" or cm_cmd == "latte" or cm_cmd == "cappuccino":
        cm_make_cup(cm_cmd)
        cm_cmd = "on"
    else:
        cm_cmd = "on"

        
        
  