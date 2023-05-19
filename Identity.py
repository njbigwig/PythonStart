#num1, num2 = 10, 10
num1 = 10
num2 = 10
num3 = num1

print("Address of variable num1 in the memory is:", id(num1))
print("Address of variable num2 in the memory is:", id(num2))
print("Address of variable num3 in the memory is:", id(num3))

print("Does num1 and num2 represent the same object?: ", num1 is num2)
print("Does num2 and num3 represent the same object?: ", num2 is num3)
print("Does num1 and num3 represent the same object?: ", num1 is num3)

print("Does num1 and num2 represent different objects?: ", num1 is not num2)
print("Does num1 and num3 represent different objects?: ", num1 is not num3)