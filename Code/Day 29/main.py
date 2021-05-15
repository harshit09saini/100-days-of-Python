# Password Manager GUI
import json
import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 12)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_length = len(letters)
    numbers_length = len(numbers)
    symbols_length = len(symbols)
    password_hard = []

    for letter in range(0, nr_letters):
        alph_index2 = random.randint(0, letters_length - 1)
        rand_index = random.randint(0, nr_letters - 1)
        password_hard.insert(rand_index, letters[alph_index2])

    for number in range(0, nr_numbers):
        num_index2 = random.randint(0, numbers_length - 1)
        rand_index = random.randint(0, nr_letters - 1)
        password_hard.insert(rand_index, numbers[num_index2])

    for symbol in range(0, nr_symbols):
        sym_index2 = random.randint(0, symbols_length - 1)
        rand_index = random.randint(0, nr_letters - 1)
        password_hard.insert(rand_index, symbols[sym_index2])

    password_hard_str = ''.join(password_hard)
    password_input.insert(0, password_hard_str)
    pyperclip.copy(password_hard_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_login():
    website = website_input.get()
    user = username_input.get()
    password = password_input.get()
    new_password = {website.title(): {
        "username": user,
        "password": password,
    }}

    if len(password) == 0 or len(user) == 0 or len(website) == 0:
        messagebox.showwarning(title="Bro what are you doing?", message="You cannot leave any field empty")
    else:
        try:
            with open("passwords.json", "r") as password_file:
                # Reading the data from the json file
                saved_passwords = json.load(password_file)
                # print(f"file read - {saved_passwords}")

        except FileNotFoundError:
            with open("passwords.json", "w") as password_file:
                # initial password writing if the file doesn't exist
                # print(f"coming from error")
                json.dump(new_password, password_file)

        else:
            # Updating saved passwords
            saved_passwords.update(new_password)
            with open("passwords.json", "w") as password_file:
                # Writing the dat to the file
                # print(f"file updated - {saved_passwords}")
                json.dump(saved_passwords, password_file, indent=4)
        finally:
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
            messagebox.showinfo(title="Info Added", message="Congrats, we've successfully stolen your login info")


def search():
    website = website_input.get().title()
    try:
        with open("passwords.json", "r") as password_file:
            saved_passwords = json.load(password_file)
    except FileNotFoundError:
        messagebox.showerror(title="Not Found", message="File does not exist.")
    else:
        if website in saved_passwords:
            messagebox.showinfo(title=website,
                                message=f"Username: {saved_passwords[website]['username']}\n"
                                        f"Password: {saved_passwords[website]['password']}")
        else:
            messagebox.showwarning(title="Entry Not Found", message=f"No Entry for {website}")
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = tk.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = tk.Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = tk.Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

username_input = tk.Entry(width=35)

username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "harshit@gmail.com")

password_input = tk.Entry(width=21)
password_input.grid(row=3, column=1)

generate_password_button = tk.Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=35, command=store_login)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
