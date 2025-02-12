# List Comprehension
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
#
# new_list = [n+1 for n in numbers]
#
# manual process to create a new list from an existing list
# numbers = [1, 2, 3]
# new_list = []
# for n in list:
#   add_1 = n + 1
#   new_list.append(add_1)

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(numbers)
print(new_list)

# also works with strings
name = "Dave"
new_name = [c for c in name]
print(name)
print(new_name)

# using range() - no base list
new_nums = [n*2 for n in range(1,5)]
print(new_nums)

# conditional - names with only 4 characters:
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# conditional example to capitalize names with length > 4
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)


