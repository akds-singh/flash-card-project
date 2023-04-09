import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------------------------- Get French Words ----------------------------------- #

# Getting the French and English word form .CSV file  and convert onto dict.
df = pandas.read_csv(filepath_or_buffer="./data/french_words.csv")
dict_data = df.to_dict(orient='split')
# print(dict_data)
# print(dict_data["data"])
from_dict_data = {item[0]: item[1] for item in dict_data['data']}


# func for choice a random word form above dict
def random_french_word():
    french_words_list = [val for val in from_dict_data.keys()]
    rand_french_word = random.choice(french_words_list)

    canvas.itemconfig(tagOrId=french_word, text=rand_french_word)


# print(from_dict_data)

# ---------------------------------------------- UI Setup ------------------------------------------- #


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas widget -----------------------------------------
canvas = tk.Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back = tk.PhotoImage(file='./images/card_back.png')
canvas.create_image(400, 270, image=card_back)

card_front = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 270, image=card_front)

canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
french_word = canvas.create_text(400, 253, text='trouve', font=('Arial', 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons Widgets --------------------------------------------------

right_sign_img = tk.PhotoImage(file="./images/right.png")
right_sign_button = tk.Button(image=right_sign_img, highlightthickness=0, bg=BACKGROUND_COLOR,
                              command=random_french_word)
right_sign_button.grid(row=1, column=0)

wrong_sign_img = tk.PhotoImage(file='./images/wrong.png')
wrong_sign_button = tk.Button(image=wrong_sign_img, highlightthickness=0, bg=BACKGROUND_COLOR,
                              command=random_french_word)
wrong_sign_button.grid(row=1, column=1)

window.mainloop()
