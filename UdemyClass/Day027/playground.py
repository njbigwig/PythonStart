
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

# include default values in a function declaration, supports optional arguements
def my_function(z, a=1, b=2, c=3):
    pass

# unlimited positional arguements
def add(*args):
    sum = 0
    print(args[0])
    print(args)
    for n in args:
        sum += n
    return sum

# **kwargs = unlimited number of keyword arguements = like a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(f"Sum = {add(0,8,10,100,47,89)}")

print(f"Result = {calculate(2, add=3, multiply=5)}")

# if constructor only had make, mode would be set to none
my_car = Car(make="Nissan", model="GT-R")
print(f"{my_car.make}")