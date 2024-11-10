import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# using len allows me to grow list without impacting randinit
whichfriend = rando_int = random.randint(0,len(friends)-1)
print(f"{friends[whichfriend]} has to pay the bill!!!!")

# print another way - select random entry from the list
print(random.choice(friends))