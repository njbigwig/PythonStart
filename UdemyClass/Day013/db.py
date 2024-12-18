def my_function():
    # Bug: range iterates from 1 to N-1
    for i in range(1, 21):
        #print(i)
        if i == 20:
            print("You got it")


my_function()

from random import randint

# Bug: dice images 0-5, but dice num = 1-6
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(f"dice_num={dice_num}")
print(dice_images[dice_num])


#Bug: does not process 1994
year = int(input("What's your year of birth?: "))

#https://en.wikipedia.org/wiki/Generation_Z
if year > 1980 and year < 1997:
    print("You are a millennial.")
elif year >= 1997:
    print("You are a Gen Z.")
    
#Bug 1: print not idented
#Bug 2: non-numeric input causes an error - try exception catch:
#  ValueError: invalid literal for int() with base 10: 'ten'
#Bug 2: missing f in print statement - F-string = formatted string literal
try:
   age = int(input("How old are you?: "))
except ValueError:
    print("You have entered in an invalid number. Please try a numerical response in the range of 1 - 100.")   
    age = int(input("How old are you?: "))

if age > 18:
    print(f"You can drive at age {age}.")
#    print("You can drive at age {age}.")
#print("You can drive at age {age}.")

#print is your friend!!!!
#Bug: input() has ==, not =, returns logical compare, not value
word_per_page = 0
pages = int(input("Number of pages: "))
#word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
print(f"word_per_page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)



