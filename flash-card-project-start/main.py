BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

from tkinter import *
import random
import pandas
import time

current_card = { }
known_words = []

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card.itemconfig(card_language, text= "Francais", fill= "black")
    card.itemconfig(card_word, text= current_card["French"], fill= "black")
    card.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    card.itemconfig(card_image, image=card_back_image)
    card.itemconfig(card_language, text="English", fill= "white")
    card.itemconfig(card_word, text=current_card["English"], fill= "white")

def word_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# front card
card = Canvas(width=800, height=526, highlightthickness=0, bg= BACKGROUND_COLOR)
card_image = card.create_image(400, 263, image=card_front_image)
card_language = card.create_text(400, 150, text="Language", font=TITLE_FONT)
card_word = card.create_text(400, 263, text="Word", font=WORD_FONT)
card.grid(column=0, row=0, columnspan=2)

# wrong button
unknown_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
unknown_button.grid(column=0, row=1)

# right button
known_button = Button(image=right_image, highlightthickness=0, bd=0, command=lambda:[word_known(), next_card()])
known_button.grid(column=1, row=1)

# if words_to_learn exists use it, otherwise use french_words
try:
    card_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    card_data = pandas.read_csv("data/french_words.csv")

to_learn = pandas.DataFrame.to_dict(card_data, orient="records")

next_card()


test = pandas.read_csv("data/french_words.csv")
test_dict = pandas.DataFrame.to_dict(card_data)



window.mainloop()