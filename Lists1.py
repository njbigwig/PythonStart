# Pyhthon lists are not - immutable
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

# slice function for lists [:2] = to the left of element[2]
JOHN_PAUL = NAMES[:2]

GEORGE_RINGO = NAMES[2:] # remainder of list from element[2]

REVERSE = NAMES[::-1] # Start : Stop : Step by -1 as we are going in reverse order

EVERY_OTHER = NAMES[::2] # Start : Stop : Step by 2, every other name

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(NAMES)
print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
print(EVERY_OTHER)