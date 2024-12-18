enemies = 1

# global constants
PI = 3.14159

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    
def increase_enemies2():
    global enemies
    
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

increase_enemies2()
print(f"enemies2 outside function: {enemies}")

print(f"Pi = {PI}")