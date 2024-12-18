from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm_menu = Menu()

cm = CoffeeMaker()

cm_moneymachine = MoneyMachine()


#cm_menuitem = cm_menu.find_drink("coke")
#print(f"{cm_menuitem.name} ${cm_menuitem.cost:.2f}")
#for ingredient in cm_menuitem.ingredients:
#    print(f"{ingredient} {cm_menuitem.ingredients[ingredient]}")
    
cm_cmd = 'on'

while cm_cmd == 'on':
    cm_cmd = input(f"What would you like {cm_menu.get_items()}? ").lower()
    
    if cm_cmd == 'off':
        print("Powering off....")
    elif cm_cmd == 'report':
        cm.report()
        cm_moneymachine.report()
        cm_cmd = 'on'
    elif cm_cmd == 'latte' or cm_cmd == 'espresso' or cm_cmd == 'cappuccino':
        cm_menuitem = cm_menu.find_drink(cm_cmd)
        if cm_menuitem.name != 'none':
            print("Found drink")
            if cm.is_resource_sufficient(cm_menuitem) == True:
                print("Resources OK.")
                
                if cm_moneymachine.make_payment(cm_menuitem.cost) == True:
                    print("Paid - dispensing...")
                    cm.make_coffee(cm_menuitem)
                else:
                    print("Sorry, you need more money")
            else:
                print("Not enough resources, please select another beverage!")
        else:
            print("Not available, please select another beverage!") 
            
        cm_cmd = 'on'       
    else:
        cm_cmd = 'on'
        
    
    
    
    
    
