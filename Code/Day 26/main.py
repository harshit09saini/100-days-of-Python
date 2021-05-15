# List Comprehension and NATO Alphabets
import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")


nato_dict = {value.letter: value.code for (key, value) in df.iterrows()}


name = input("Enter your name: ").upper()

name_nato = [nato_dict[letter] for letter in name]
print(name_nato)

# sentence = "What is the airspeed velocity of an unladen swallow?"
# words = sentence.split(" ")
# word_len = {word:len(word) for word in words}
# print(word_len)
# with open("file1.txt") as file1:
#     data1 = file1.readlines()
#     list1 = []
#     for num in data1:
#         list1.append(num.strip())
#
# with open("file2.txt") as file2:
#     data2 = file2.readlines()
#     list2 = []
#     for num in data2:
#         list2.append(num.strip())
#
# common_list = [int(number) for number in list1 if number in list2]
# print(common_list)
