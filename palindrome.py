def PalindromeCheck(candidatestring):
    replacelist = [' ', '\t', '.', '!', ',', '?', '\\', '/', '-', ':', ';', '`', '\'', '\n' ]
        
    # remove all white space and punctuation
    for letter in candidatestring:
        if letter in replacelist:
            candidatestring = candidatestring.replace(letter,"")
            
        # match letter:
        #     case " ":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case "\t":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case ".":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case "!":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case "?":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case "\\":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case "/":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case "-":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case ",":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case ";":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case ":":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case "'":
        #         candidatestring = candidatestring.replace(letter,"")
        #     case "`":
        #         candidatestring = candidatestring.replace(letter,"")
    
    
    # use the slice operator to reverse the string
    reversestring = candidatestring[::-1]
    
    print(candidatestring)
    print(reversestring)
    
    # a string is a Palidrome if the regular and reversed strings are the same
    if ( candidatestring == reversestring ):
        checkresult = True
    else:
        checkresult = False
    
    return checkresult


def main():
    print("Palindrome Test Script")

    exitloop = False
    
    while exitloop == False:
        inputstring = input("Enter string to test: ")
        
        lowercasestring = inputstring.lower()
                
        if ( lowercasestring == "exit"):
            exitloop = True
        else:
            if ( PalindromeCheck(lowercasestring) == True ):
                print("Your string is a Palindrome!\n")
            else:
                print("Your string is NOT a Palindrome.\n") 
    

if __name__ == "__main__":
    main()