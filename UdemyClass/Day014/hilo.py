import random
import os
import logo
import followerdata

wrong_flag = False

score = 0

prompt1 = 0
prompt2 = 0

#print(type(followerdata.gamedata))
#print(len(followerdata.gamedata))

prompt2 = random.randint(0,len(followerdata.gamedata)-1)

os.system('cls')
 
while wrong_flag == False:    
    prompt1 = prompt2
    
    # get a second unique random prompt
    while prompt2 == prompt1:
        prompt2 = random.randint(0,len(followerdata.gamedata)-1)
           
    print(logo.logo)
    print("\n")
        
    print(f"Compare A: {followerdata.gamedata[prompt1]["name"]}, a {followerdata.gamedata[prompt1]["description"]}, from {followerdata.gamedata[prompt1]["country"]}")
     
    print(logo.vs)
            
    print(f"Compare B: {followerdata.gamedata[prompt2]["name"]}, a {followerdata.gamedata[prompt2]["description"]}, from {followerdata.gamedata[prompt2]["country"]}\n")
    
    choice = input("\nWho has more followers? Type 'A' or 'B: ").upper()
    
    #print(f"{followerdata.gamedata[prompt1]["follower_count"]} {followerdata.gamedata[prompt2]["follower_count"]}")
    if choice == 'A':
        if followerdata.gamedata[prompt1]["follower_count"] > followerdata.gamedata[prompt2]["follower_count"]:
            score += 1
            os.system('cls')
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong! Final score: {score}")
            wrong_flag = True
    elif choice == 'B':
        if followerdata.gamedata[prompt2]["follower_count"] > followerdata.gamedata[prompt1]["follower_count"]:
            score += 1
            #prompt1 = prompt2
            os.system('cls')
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong! Final score: {score}")
            wrong_flag = True  
    else:
        print("Invalid choice, game over!")  
        wrong_flag = True  
        
       
    
    

    