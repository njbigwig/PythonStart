fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit + " pie")

fruitindex = 0
for fruit in fruits:
    print(f"{fruitindex}  = {fruits[fruitindex]}")
    fruitindex += 1

student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
print(f"Total via sum(): {total_score}\n")

scoreidx = 0
scoresum = 0
for score in student_scores:
    scoresum += student_scores[scoreidx]
    scoreidx += 1

print(f"Total via for-loop #1: {scoresum}\n")

scoresum = 0
for score in student_scores:
    scoresum += score
    
print(f"Total via for-loop #2: {scoresum}\n")

print(f"Max score = {max(student_scores)}")
print(f"Min score = {min(student_scores)}")

highscore = 0
lowscore = 888

for score in student_scores:
    if score > highscore:
        highscore = score
    if score < lowscore:
        lowscore = score

print(f"High = {highscore} Low = {lowscore}")

# use range function
step = 2
for number in range (1,11, step):
    print(number)
    
# Gauss Challenge
gausssum = 0
for number in range (1,101):
    gausssum += number
    
print(gausssum)

