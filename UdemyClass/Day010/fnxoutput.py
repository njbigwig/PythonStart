# single return function
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    print(f"In the function {formated_f_name} {formated_l_name}")    
    return f"{formated_f_name} {formated_l_name}"

# docstrings help document a function so the syntax is shown in an editor, must be first line of the function
# multiple returns
def is_leap_year(year):
    """Evaluates if year is a leap year:\n
          year is evenly divisible by 4 AND not equally divisible by 100 OR\n
          year is evenly divisible by 4 AND year is equally divisible by 400"""
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

firstname = input("What is your first name?: ")
lastname = input("What is your last name?: ")

formatted_name = format_name(firstname, lastname)
print(f"{formatted_name}")

for whatyear in range(1966,2024):
    print(f"{whatyear} is a leap year? {is_leap_year(whatyear)}")
    
    