# function with no parameters
# def greet():
#     print("Hello!")
#     print("What is your name?")
#     print("My name is Yoda!")
 
# function with 1 parameter   
# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print("My name is Yoda!")

# functions with more than 1 input
def greet_with_name_location(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
    
def calculate_love_score(name1, name2):
    name1cnt = 0
    name2cnt = 0
    
    name1allcaps = name1.upper()
    name2allcaps = name2.upper()
            
    truelist =['T', 'R', 'U', 'E']
    lovelist =['L', 'O', 'V', 'E']
    
    for char in truelist:

        if name1allcaps.count(char) > 0:
            name1cnt += name1allcaps.count(char) 
        if name2allcaps.count(char) > 0:
            name1cnt += name2allcaps.count(char) 
        
            
    for char in lovelist:
        if name1allcaps.count(char) > 0:
            name2cnt += name1allcaps.count(char)
        if name2allcaps.count(char) > 0:
            name2cnt += name1allcaps.count(char) 
            
    print(f"{name1cnt}{name2cnt}")
            
calculate_love_score("Kanye West", "Kim Kardashian") 
    
#greet()

#greet_with_name("Darth")

#greet_with_name_location("Bigwig", "Watership Down")

# keyword arguements
#greet_with_name_location(name="Bigwig", location="Watership Down")
#greet_with_name_location(location="Watership Down", name="Bigwig")