import  tkinter as tk

window = tk.Tk()
window.config(pady=50, padx=50)

canvas = tk.Canvas(width=800, height=550, bg='gray75')

front = tk.PhotoImage(file="./images/card_front.png")
back = tk.PhotoImage(file="./images/card_back.png")
# canvas.create_image(400, 275, image=front)
canvas.create_image(400, 275, image=back)

canvas.grid(row=0,column=0)



window.mainloop()