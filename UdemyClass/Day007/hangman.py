# thanks for the hint Copilot!
from wonderwords import RandomWord

from hangmanart import stages

rw = RandomWord()

max_guesses = 6

guessword = rw.word()

print(f"Random Word: {guessword} Len = {len(guessword)}")

print("Welcome to Hangman\n")
print(f"You have {max_guesses} guesses to try to guess the word...")

wordlen = len(guessword)
guesses = max_guesses # was wordlen, but needed to account for ASCII art

userguessstr = ""

for char in range(wordlen):
    userguessstr += "*"
    
userguesslist = list(userguessstr)

while guesses > 0 and '*' in userguesslist:
    print (f"Word to guess: {"".join(userguesslist)}")
    print(f"*** You have {guesses} out of {max_guesses} remaining ***\n")
    
    guesschar = input("Guess a letter: ").lower()
    
    if userguesslist.count(guesschar):
       print(f"You have already guessed {guesschar}")
    elif guessword.find(guesschar) >= 0:
        print("Correct!\n\n")
        
        # populate the user guess list with the correct guess character
        for char in range(wordlen):
            if guessword[char] == guesschar:
                userguesslist[char] = guesschar            
    else:
        guesses -= 1
        print(f"Your guessed {guesschar}, that's not in the word. You lose a life\n")
    
    print(stages[guesses])
            
if not '*' in userguesslist:
    print(f"You guessed the correct word {guessword}!")
else:
    print(f"Sorry, you lost. The word was {guessword}.")
    
#for s in stages:
#    print(f"{s}")

#for x in range(3):
#    mystr = ""
#   for chr in guessword:
#       mystr += chr
#   print(f"{mystr}")
    
        