# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.read().split("\n")
    print(names_list)

# Replace the [name] placeholder with the actual name.

with open("./Input/Letters/starting_letter.txt") as letters:
    content = letters.read()
    for name in names_list:
        new_letter = content.replace("[name]", name)

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letters_to_send:
            letters_to_send.write(new_letter)
        print(new_letter)

# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
