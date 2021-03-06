import csv
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily", "Stewart"],
    "score": [56, 76, 98, 52]
}

print("LOOP THROUGH DICTIONARY:")
print('for (key,value) in student_dict.items(): ')
print('print(key)')
print('print(value)')
print('#######################################')
#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key)
    print(value)
    pass
print('#######################################')
import pandas
student_data_frame = pandas.DataFrame(student_dict)

print('PRINTING DATAFRAME:')
print('student_data_frame = pandas.DataFrame(student_dict)')
print('student_data_frame.head(20)')
print(student_data_frame.head(20))      #prints the head of the data frame  with index, column headings and data

print('#######################################')
print('LOOP THROUGH DATAFRAME: ')
print('for(index, row) in student_data_frame.iterrows(): ')
print('print(index)')
print('print(row)')
print('print(row.student')
print('print(row.score)')
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
        print(index)
        print(row)
        print(row.student)
        print(row.score)
        pass
print('#######################################')

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import csv
import pandas

######################
#LECTURE SOLUTION:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}  #can row be replaced with 'cell' instead?
#a row seems to be an entire horizontal line.  this appears to be iteratting through individual cells or entries in the
# letter and code columns.  picture a pointer pointing to first entry in columns titled letter and code.
#data.iterrows then causes the pointers to advance to the next entry in the column.  cell 0 in letter column.  cell 0 in
#code column.  then cell 1 in letter column.  cell 1 in code column.  then on and on.

phonetic_dict = {column.letter:column.code for (index, column) in data.iterrows()}  #THIS WORKS THE SAME AS LECTURE
#SOLUTION.  A LITTLE EASIER TO UNDERSTAND.  UNCLEAR ON HOW index is working or iterrows.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
#messy way would but to declare output_list = []
#then for letter in word:
#output_list.append(phonetic_dict[letter])
#so formatting to remember is when doing a comprehensive list or dictionary, the thing to be appended goes first.
#then the for loop is written.

print(output_list)

######################
#nato_dict ={}
#opens file. DOES NOT  reads into data frame.  FORGOT
#TO USE PANDAS.  INSTEAD WROTE INTO readcsv object.
#WHOOPS!
#iterates through key value pairs in readcsv object
#into nato_dict.  but first entry is 'letter': 'code' pair
#then use pop with key 'letter' and column headings
#are removed from dictionary
# with open("nato_phonetic_alphabet.csv") as nato_phonetic_file:
#      nato_dataframe = csv.reader(nato_phonetic_file)
#      nato_dict = {index:row for(index, row) in nato_dataframe}
#          #print(index)
#          #print(row)

# print(nato_dict)
#
# #THIS REMOVES ENTRY IN THE DICTIONARY WITH KEY 'letter'
# nato_dict.pop('letter')
# print(nato_dict)
# #
# name = input("ENTER YOUR NAME. ").upper()
# #use append as mental model
# #whatever is to be appended goes first
# #then ordinary for loop
# code_list=[nato_dict[letter] for letter in name]
#
# #was able to make list by using append.
# #if stuck again take stuff out of append
# #method place in front of for and place all between
# #brackets and should work.
# # for letter in name:
# #     code_list.append(nato_dict[letter])
# #
# print(code_list)




# with open("nato_phonetic_alphabet.csv") as nato_phonetic_file:
#     print(nato_phonetic_file)
#     reader = csv.reader(nato_phonetic_file)
#     print(reader)
#     nato_dict = {rows[0]: rows[1] for rows in reader}
#
# print(nato_dict)

#import csv
# reader = csv.reader(open('nato_phonetic_alphabet.csv', 'r'))
# nato_dict = {}
# for row in reader:
#     k,v = row
#     nato_dict[k] =v
# print(nato_dict)

import pandas

#nato_dict = {row[0]: row[1] for _, row in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

#print(nato_dict)

#name = input("Enter your name. ").upper()

#nato_list =[]
# for letter in name:
#     nato_list.append(nato_dict[letter])

#nato_list = [letter for letter in nato_dict[letter]]

#print(nato_list)

#with open('nato_phonetic_alphabet.csv') as nato_file:
#    nato_dict = {letter:code for (letter,code) in nato_file}

#print(nato_dict)
###############################################
#BELOW WORKS
###############################################
#import csv
# with open('nato_phonetic_alphabet.csv') as infile:
#     reader = csv.reader(infile)
#     natodict={rows[0]: rows[1] for rows in reader}
#
# name = input("Enter your name. ").upper()
# nato_list=[]
# for letters in name:
#     nato_list.append(natodict[letters])
#
# print(nato_list)
####################################################
# import pandas
#
# nato_dict = {col[0]: col[1] for col, col in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
#
# print(nato_dict)
#
# #name = input("ENTER YOUR NAME. ")
#
#
# nato_list =[]
#
# for (key,value) in nato_dict.items():
#     if value in nato_dict.items():
#         nato_list.append(value)
#
# print(nato_list)
#
#
