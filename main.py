import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
after_ids_list = []
rand_item = {}
is_right_sign_clicked = 0
is_wrong_sign_clicked = 0
words_data_list = []


def on_right_sigh_clicked():
    next_card()
    save_into_words_to_learn_csv_file()


def on_cross_sign_clicked():
    next_card()


# --------------------------------------------- Get Words From CSV File ----------------------------------- #

# Getting the French and English word form .CSV file  and convert onto list of dict.-----

def load_data():
    global words_data_list
    try:
        df = pandas.read_csv(filepath_or_buffer="./data/words_to_learn.csv")
    except FileNotFoundError:
        df = pandas.read_csv(filepath_or_buffer="./data/french_words.csv")
        words_data_list = df.to_dict(orient='records')
    else:
        words_data_list = df.to_dict(orient='records')


# ------------------------------Create CSV file to save words  that need to learn -----------------------#
def save_into_words_to_learn_csv_file():
    # load all data  to words_to_learn.csv file form words_data_list
    words_data_list.remove(rand_item)
    df = pandas.DataFrame(words_data_list)
    df = df[['French', 'English']]
    df.to_csv('./data/words_to_learn.csv', index=False)


# func for choice a random word form words_data_list------------------

def next_card():
    global after_ids_list, rand_item
    rand_item = random.choice(words_data_list)
    french_word = rand_item['French']

    canvas.itemconfig(tagOrId=card_front, state='normal')
    canvas.itemconfig(tagOrId=title_word, text='French', fill='black')
    canvas.itemconfig(tagOrId=text_word, text=french_word, fill='black')

    after_id = window.after(ms=3000, func=flip_card)
    after_ids_list.append(after_id)

    for val in range(0, len(after_ids_list) - 1):
        val_str = after_ids_list[val]
        window.after_cancel(val_str)
        after_ids_list.pop(val)


# ---------------------------------------------flip card function ---------------------------------------#
def flip_card():
    global after_ids_list
    canvas.itemconfig(tagOrId=card_front, state='hidden')
    canvas.itemconfig(tagOrId=title_word, text='English', fill='white')
    canvas.itemconfig(tagOrId=text_word, text=rand_item['English'], fill='white')


# ---------------------------------------------- UI Setup ------------------------------------------- #

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
load_data()
# Canvas widget -----------------------------------------
canvas = tk.Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back_img = tk.PhotoImage(file='./images/card_back.png')
card_back = canvas.create_image(400, 270, image=card_back_img)

card_front_img = tk.PhotoImage(file="./images/card_front.png")
card_front = canvas.create_image(400, 270, image=card_front_img)

title_word = canvas.create_text(400, 150, text='Language', font=('Arial', 40, 'italic'))
text_word = canvas.create_text(400, 253, text='Word', font=('Arial', 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons Widgets --------------------------------------------------

right_sign_img = tk.PhotoImage(file="./images/right.png")
right_sign_button = tk.Button(image=right_sign_img, highlightthickness=0, bg=BACKGROUND_COLOR,
                              command=on_right_sigh_clicked)

right_sign_button.grid(row=1, column=0)

cross_sign_img = tk.PhotoImage(file='./images/wrong.png')
cross_sign_button = tk.Button(image=cross_sign_img, highlightthickness=0, bg=BACKGROUND_COLOR,
                              command=on_cross_sign_clicked)
cross_sign_button.grid(row=1, column=1)

window.mainloop()
