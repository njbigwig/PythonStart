#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
 
# get the form letter content       
with open("input\\Letters\\starting_letter.txt") as letterfile:
    lettercontents = letterfile.read()
    #print(lettercontents)
    
# get the names
namelist = []
with open("input\\Names\\invited_names.txt") as namefile:
    namelist = namefile.readlines()
    
for name in namelist:
    newname = name.strip()
    print(f"Creating letter for [{newname}]")
    newlettercontents = lettercontents
    letterfilename = "Output\\ReadyToSend\\" + newname + ".txt"
    #print(newlettercontents)
    #print(letterfilename)
    
    # add name to file
    customlettercontents = newlettercontents.replace("[name]", newname)
    #print(customlettercontents)
    
    # write new custom letter
    with open(letterfilename, mode="w") as inviteletterfile:
        inviteletterfile.write(customlettercontents)
  
