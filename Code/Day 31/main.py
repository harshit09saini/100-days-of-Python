# Flash Card App
import tkinter as tk
import time
import random

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# STEPS

# Make a window and add the front image, right, and wrong
# Import words using pandas
# Create a list for each language
# Create a "learned" list and add the word if clicked on yes
# if no, then move the word back into the language list
# Remove the learned word from the full list
# Set a timer for 3 seconds to show the meaning

# ============================= WORDS ============================= #

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")

words_dict = df.to_dict(orient="records")

random_word = {}


def get_new_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(words_dict)
    canvas.itemconfig(canvas_image, image=image_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word_label, text=random_word["French"], fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=image_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word_label, text=random_word["English"], fill="white")


def is_known():
    words_dict.remove(random_word)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    get_new_word()




# ============================= UI ============================= #

window = tk.Tk()
window.title("Flash Cards")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

# Card images
image_front = tk.PhotoImage(file="images/card_front.png")
image_back = tk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 300, image=image_front)
canvas.grid(row=0, column=0, columnspan=2)

# Button Images
image_wrong = tk.PhotoImage(file="images/wrong.png")
button_wrong = tk.Button(image=image_wrong, highlightthickness=0, command=get_new_word)
button_wrong.grid(row=1, column=0)

image_correct = tk.PhotoImage(file="images/right.png")
button_correct = tk.Button(image=image_correct, highlightthickness=0, command=is_known)
button_correct.grid(row=1, column=1)

# Canvas Text

language = canvas.create_text(400, 150, text="Title", font=("Aerial", 30, "italic"))
word_label = canvas.create_text(400, 300, text="Word", font=("Aerial", 70, "bold"))

flip_timer = window.after(3000, flip_card, random_word)
get_new_word()

window.mainloop()
