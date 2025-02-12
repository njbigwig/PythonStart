import pandas


#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
#    #Access index and row #   #Access row.student or row.score
#    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

print("Reading NATO CSV file with Pandas....")
natoalphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
print(type(natoalphabet))


nato_dict = {row.letter:row.code for (index, row) in natoalphabet.iterrows()}
print(nato_dict)
print("\n")

# for (index, row) in natoalphabet.iterrows():
#     print(index)
#     print(row.letter) # Pandas series object - shows just the names
#     print(row.code) # Pandas series object - shows just the scores

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
myword = input("Enter in a word: ").upper()
mywordlist = list(myword)

# create a list with the NATO alphabet
natowordlist = [nato_dict[letter] for letter in mywordlist]
print(natowordlist)


