from tkinter import *
import pandas
import random
# import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(language_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=current_card["French"], fill="black")
    canvas.itemconfig(create_image, image=flashcard_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(create_image, image=flashcard_back_img)
    canvas.itemconfig(language_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=current_card["English"], fill="white")

def is_known():
    data_dict.remove(current_card)
    learn_data = pandas.DataFrame(data_dict)
    learn_data.to_csv("data/words_to_learn.csv", index = False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
flashcard_front_img = PhotoImage(file="images/card_front.png")
create_image = canvas.create_image(400,263, image=flashcard_front_img)
flashcard_back_img = PhotoImage(file="images/card_back.png")
language_txt = canvas.create_text(400,150,font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400,263, font=("Ariel", 60, "bold"))
canvas.grid(column = 0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(highlightbackground=BACKGROUND_COLOR, highlightthickness=0, image=right_img, command=is_known)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(highlightbackground=BACKGROUND_COLOR, highlightthickness=0, image=wrong_img, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()