from tkinter import *
from tkinter import Canvas
import pandas
import random
# ---------------------------------GENERATE---------------------------------
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# ---------------------------------SAVING---------------------------------
try:
    data = pandas.read_csv("./GUI-tkinter/flash-card-app/data/words_to_learn.csv")
    data.columns = data.columns.str.strip() # Fix Whitespaces
except (FileNotFoundError, pandas.errors.EmptyDataError): # File not exsist, empty
    original_data = pandas.read_csv("./GUI-tkinter/flash-card-app/data/french_words.csv")
    original_data.columns = original_data.columns.str.strip() # Fix Whitespaces
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------------BUTTON---------------------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./GUI-tkinter/flash-card-app/data/words_to_learn.csv", index=False)
    next_card()
    
# ---------------------------------UI SETUP---------------------------------
window = Tk()
window.title("Flask Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=529, width=800)
card_front_img = PhotoImage(file="./GUI-tkinter/flash-card-app/images/card_front.png")
card_back_img = PhotoImage(file="./GUI-tkinter/flash-card-app/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 20, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image =  PhotoImage(file="./GUI-tkinter/flash-card-app/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image =  PhotoImage(file="./GUI-tkinter/flash-card-app/images/right.png")
check_button= Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()