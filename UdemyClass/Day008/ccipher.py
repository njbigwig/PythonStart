# Caesar Cipher
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encoder = []
    encoded_str = ""
    
    charcnt = 0
    char_source_idx = shift_amount
    char_destinstation_idx = 0
    
    # create the encoder list:
    #  TODO - try using list function to map lists
    for charcnt in range(26):
        encoder.insert(char_destinstation_idx, alphabet_list[char_source_idx])
        
        # modulus to wrap to 0 when source index > 25
        char_source_idx = (char_source_idx + 1) % len(alphabet_list)
                
        char_destinstation_idx += 1
        
    #print(f"encoder list[]: {encoder}")
    for character in original_text:
        if character.isalpha():
             encoded_str += encoder[ord(character)-ord('a')]
        else:
           encoded_str += character
    
    print(f"Here's the encoded result: {encoded_str}")
    
def decrypt(original_text, shift_amount):
    encoder = []
    decoded_str = ""
    
    charcnt = 0
    char_source_idx = shift_amount
    char_destinstation_idx = 0
    
    # create the encoder list:
    #  TODO - try using list function to map lists
    for charcnt in range(26):
        encoder.insert(char_destinstation_idx, alphabet_list[char_source_idx])
        
        # modulus to wrap to 0 when source index > 25
        char_source_idx = (char_source_idx + 1) % len(alphabet_list)
                
        char_destinstation_idx += 1
        
    #print(f"encoder list[]: {encoder}")
    for character in original_text:
        if character.isalpha():
            decoded_str += alphabet_list[encoder.index(character)]
        else:
            decoded_str += character
    
    print(f"Here's the decoded result: {decoded_str}")
    
# get the ASCII value of 'a' = 97 = 0x61
#print(ord('a'))    

done = False

while done == False:
    cmd = input("Type \'encode\' to encrypt, type  \'decode\' to decrypt: ")

    user_text = input("Type your message: ")

    shift_number = 0
    while shift_number == 0:
        shift_number = int(input("Type the LEFT shift number: "))
        if shift_number <= 1 or shift_number > 20:
            print("ERROR: shift number must be > 1 and < 21")
            shift_number = 0

    if cmd.lower() == "encode":
        encrypt(user_text.lower(), shift_number)   
    else:
        decrypt(user_text.lower(), shift_number) 
        
    cmd = input("Type \'yes\' if you want to go again. Otherwise type  \'no\'.\n")
    if cmd.lower() == "no":
        done = True
        
   