
morse_encoder={
    "A": ". - ",
    "B": "- . . . ",
    "C": "- . - . ",
    "D": "- . . ",
    "E": ". ",
    "F": ". . - . ",
    "G": "- - . ",
    "H": ". . . . ",
    "I": ". . ",
    "J": ". - - - ",
    "K": "- . - ",
    "L": ". - . . ",
    "M": "- - ",
    "N": "- . ",
    "O": "- - - ",
    "P": ". - - . ",
    "Q": "- - . - ",
    "R": ". - . ",
    "S": ". . . ",
    "T": "- ",
    "U": ". . - ",
    "V": ". . . - ",
    "W": ". - - ",
    "X": "- . . - ",
    "Y": "- . - - ",
    "Z": "- - . . ",
    " ": "___",
    "0": "- - - - - ",
    "1": ". - - - - ",
    "2": ". . - - - ",
    "3": ". . . - - ",
    "4": ". . . . - ",
    "5": ". . . . . ",
    "6": "- . . . . ",
    "7": "- - . . . ",
    "8": "- - - . . ",
    "9": "- - - - . "
}

regular_text = input("Enter your message: ").upper()

print(regular_text)

for character in regular_text:
    if (character >= 'A' and character <= 'Z') or (character >= '0' and character <= '9') or character == ' ':
        print(morse_encoder[character])