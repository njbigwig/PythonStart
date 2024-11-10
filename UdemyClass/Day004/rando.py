# Random numbers

import random
# can import other py files to shorten file length

# random.randint(a, b) Random integer N, such that a <= N <= b
rando_int = random.randint(1,10)
print(f"random int number: {rando_int}\n")

# 2 ways of getting a randon float between 0 and 10

# includes 0
rando_float1 = random.random() * 10
print(f"random float number 1: {rando_float1}\n")

# starts at 1
rando_float2 = random.uniform(1, 10)
print(f"random float number 2: {rando_float2}\n")

print(random.choice(["rock", "paper", "scissors"]))

# coin flip
print("Flipping a coin: heads or tails....")
rando_float1 = random.randint(0,1)
if rando_float1 == 0:
    print("Heads")
else:
    print("Tails")
