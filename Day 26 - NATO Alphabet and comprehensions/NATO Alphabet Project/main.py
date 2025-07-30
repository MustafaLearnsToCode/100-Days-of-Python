import pandas
from logo import logo

#Looping through dictionaries:
#for (key, value) in student_dict.items():
#     Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
#     Access index and row
#     Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(nato_dict)

#Create a list of the phonetic code words from a word that the user inputs.
print(logo)
print("Welcome to the NATO Alphabet Converter")
word = input("Please enter your word: ").upper()
nato_word = [nato_dict[letter] for letter in word]
print(nato_word)
