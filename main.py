import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
after_ids_list = []
eng_word = ''


# ---------------------------------------------flip card func ---------------------------------------#
def flip_card():
    global after_ids_list
    # print(after_ids_list)
    # window.after_cancel(after_ids_list)
    # canvas.itemconfig(tagOrId=card_back, state='normal')
    canvas.itemconfig(tagOrId=card_front, state='hidden')
    canvas.itemconfig(tagOrId=title_word, text='English', fill='white')
    canvas.itemconfig(tagOrId=text_word, text=eng_word, fill='white')

    print("card flip")


# --------------------------------------------- Get Words From CSV File ----------------------------------- #

# Getting the French and English word form .CSV file  and convert onto list of dict.-----
df = pandas.read_csv(filepath_or_buffer="./data/french_words.csv")
list_data = df.to_dict(orient='records')


# print(list_data)

# func for choice a random word form above dict------------------
def random_words():
    global after_ids_list, eng_word
    print(after_ids_list)
    # french_words_list = [val for val in dict_from_list_data.keys()]
    rand_item = random.choice(list_data)
    print(rand_item)
    french_word = rand_item['French']
    eng_word = rand_item['English']
    canvas.itemconfig(tagOrId=card_front, state='normal')
    canvas.itemconfig(tagOrId=title_word, text='French', fill='black')
    canvas.itemconfig(tagOrId=text_word, text=french_word, fill='black')

    after_id = window.after(ms=3000, func=flip_card)
    after_ids_list.append(after_id)

    for val in range(0, len(after_ids_list)-1):
        val_str = after_ids_list[val]
        window.after_cancel(val_str)
        after_ids_list.pop(val)
    # window.after_cancel(after_ids_list)


# ---------------------------------------------- UI Setup ------------------------------------------- #


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# after_ids_list = window.after(ms=3000, func=flip_card)
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
right_sign_button = tk.Button(image=right_sign_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_words)
right_sign_button.grid(row=1, column=0)

wrong_sign_img = tk.PhotoImage(file='./images/wrong.png')
wrong_sign_button = tk.Button(image=wrong_sign_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_words)
wrong_sign_button.grid(row=1, column=1)

window.mainloop()
