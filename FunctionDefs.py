#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
# https://www.linkedin.com/learning/learning-python-14393370/
#


# define a basic function
def func1():
    print("I am function #1")

# function that takes arguments
def func2(arg1, arg2):
    print("Function arguements: ", arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x ** 3

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


print("Function #1")
func1()
print("Func1():", func1()) # function called, but does not return anything = none
print("Func1:", func1)
print("Type of func1:", type(func1))
print("\n")

print("Function #2")
func2(10, 20)
print(func2(10,20))
print("Cube(3) = ", cube(3))
print("\n")

print("Function #3")
print("power(2) = ", power(2))
print("power(2,3) = ", power(2,3))
print("Python can handle parameters in different order power(x=3, num=2) = ", power(x=3, num=2))
print("\n")

print("Function #4")
print("multi_add with no arguements: ", multi_add())
print("multi_add with arguements: ", multi_add(4,5,10,4))
print("\n")

