from tkinter import *
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
SECONDS = 3

timer = None
current_card = {}
to_learn = {}




try:
    french_words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_french_words_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_french_words_data.to_dict(orient="records")
else:
    to_learn = french_words_data.to_dict(orient="records")




window = Tk()
window.config(width=850, height=776, bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")


def is_known():
    global current_card, to_learn
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    flash_card()
#    print(guessed_words)
    print(len(to_learn))


def flip_card(word):
    global back_img
    canvas.create_image(400, 263, image=back_img
                        )
    canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"))
    canvas.create_text(400, 263, text=current_card["English"], font=("Arial", 60, "bold"))


def flash_card():
    global front_img, english_words, timer, current_card, to_learn
    if timer is not None:
        window.after_cancel(timer)

    # word_pair = get_new_word()
    current_card = random.choice(to_learn)
    # current_card = word_pair[0]
    # word_index = word_pair[1]

    canvas.create_image(400, 263, image=front_img)
    canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
    canvas.create_text(400, 263, text=current_card["French"], font=("Arial", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    # english_word = english_words[word_index]

    timer = window.after(3000, flip_card, current_card)
    # print(guessed_words)
    # print(current_card)

    # if stop is True:
    #     flip_card(english_word)
    # pass


# Buttons
wrong_button = Button(window, image=wrong_img, highlightthickness=0, command=flash_card)
wrong_button.grid(column=0, row=1)

right_button = Button(window, image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

flash_card()

window.mainloop()
