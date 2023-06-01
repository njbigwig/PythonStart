greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

# method #1 to add a variable parameter to an immutable string
intrupution = f"Hello {name}"

# method #2 to add a variable parameter to an immutable string
greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Ringo"))