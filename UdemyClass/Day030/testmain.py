# will generate an error - FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError KeyError: 'no_existent_key'
# a_dictionary = {"key": "value"}
# value = a_dictionary["no_existent_key"]

# IndexError IndexError: list index out of range
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# TypeError TypeError: can only concatenate str (not "int") to str
# text = "abc"
# print(text + 5)

# Python exceptions
# try:
# except:
# else:
# finally:

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     #value = a_dictionary["no_existent_key"]
#     value = a_dictionary["key"]
# except FileNotFoundError:
#     print("there was an error - recover by creating file...")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"Key {error_message} does not exist")
# else:
#     print("everthing is fine")
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")
#     # raise our own exception
#     raise KeyError("Blah Blah")

height = float(input("Height m: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")

weight = int(input("Weight kg: "))
bmi = weight/(height ** 2)
print(bmi)

    
    
    


    