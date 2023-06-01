NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

print("Names: ", NAMES)
print("Ages: ", AGES)

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

# zips the lists together, but does not modify the original lists
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate: enumerate(iterable, start index=0)
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
    
# enumerate can also be used for a string
print(list(enumerate(NAMES[2])))
