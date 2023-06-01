number = int(input("Enter a number: "))

if ( number > 0 ):
    print("Entered inside the parent if block")
 
    if ( number > 10 ):
        print("Entered inside the nested if block")  
        
    print("Control flows back into the parent if block") 

print("Control flows out of the parent block")