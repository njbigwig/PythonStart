# can reference a string via an array operator (subscriptor) - first character
print("Hello"[0])

# print the last character #1
print("Hello"[len("Hello")-1])

# print the last character #2
print("Hello"[-1])

# integer
print(123 + 456)

# large integer _ represents comma
print(123_456_789)

# floating point number
print(3.14159)

# boolean
print(True)
print(False)

# fix the error
print(len("12345"))

# finding type of variables
print(type("12345"))
print(type(12345))
print(type(12345.12345))
print(type(123_123_123))
print(type(True))

# type casting
print(int("123") + int("456"))

# fix this
#print("Number of letters in your name: " + str(len(input("Enter your name "))))

print(6/5)
print(6//5) # modulus

# x to the y power
print(2**3)

# mathematical precedence PEMDAS
# (3*3 + 3/3 - 3) => (9 + 1 - 3) => (9 - 2) => 7
print(3*3 + 3/3 - 3) 

bmi = 84/1.65**2
print(bmi)
print(int(bmi))

# use round to truncate float
print(round(bmi,2))

# f-string = format parameters like C printf()
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height = {height}, you are winning = {is_winning}")





