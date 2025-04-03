# with corrections
import tkinter
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
words_to_learn = []
flip_id = None

def is_known():
    pass

def card_flip():
    global current_card
        
    canvas.itemconfigure(image_id, image=back_logo_image)
    
    canvas.itemconfig(titletext_id,fill='white')
    canvas.itemconfig(wordtext_id,fill='white')
    
    canvas.itemconfig(titletext_id, text="English")
    canvas.itemconfig(wordtext_id, text=current_card["English"])
    
    
def next_card():
    global current_card
    global flip_id
    # alternative: frenchword = random.choice(worddata_dictionary), then worddata_dictionary.pop(0)
    #frenchword = worddata_dictionary.pop(0)
    
    window.after_cancel(flip_id)
    
    canvas.itemconfigure(image_id, image=front_logo_image)
    canvas.itemconfig(titletext_id,fill='black')
    canvas.itemconfig(wordtext_id,fill='black')
    
    if len(worddata_dictionary) > 0:
        current_card = worddata_dictionary.pop(0)
       
    canvas.itemconfig(titletext_id, text="French")
    canvas.itemconfig(wordtext_id, text=current_card["French"])
    
    flip_id = window.after(3000, card_flip)   
         
    
def save_card():
    global current_card
    global flip_id
    global words_to_learn
    
    words_to_learn.append(current_card)
    #print(words_to_learn)
    
    # update CSV file for words we need to learn
    words_to_learn_dataframe = pandas.DataFrame(words_to_learn)
    words_to_learn_dataframe.to_csv("data\\words_to_learn.csv", index=False)    
    
    next_card()
    
        
def print_coordinates(event):
    x = event.x
    y = event.y
    print(f"Clicked at: x={x}, y={y}")
   
    
# program window frame with 50 pixel padding
window = tkinter.Tk()
window.title("Frenchy Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# create canvas to attach items to
canvas = tkinter.Canvas(width=800, height=526)

# add the card front image to the canvas
front_logo_image = tkinter.PhotoImage(file='images\\card_front.png')
image_id = canvas.create_image(400, 263, image=front_logo_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# create the back of the card image
back_logo_image = tkinter.PhotoImage(file='images\\card_back.png')

# text labels
titletext_id = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
wordtext_id = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

correct_image = tkinter.PhotoImage(file="images\\right.png")
correct_button = tkinter.Button(command=next_card, highlightthickness=0, image=correct_image)
correct_button.grid(row=1, column=1)

incorrect_image = tkinter.PhotoImage(file="images\\wrong.png")
incorrect_button = tkinter.Button(command=save_card, highlightthickness=0, image=incorrect_image)
incorrect_button.grid(row=1, column=0)

try:
    worddata_dataframe = pandas.read_csv("data\\words_to_learn.csv")
except FileNotFoundError:
    worddata_dataframe = pandas.read_csv("data\\french_words.csv")
    #print(f"Data Frame {worddata_dataframe}")   
finally:
    worddata_dictionary = worddata_dataframe.to_dict(orient="records")


# print(worddata_dictionary)
# print(worddata_dictionary[0])

# shuffle words
random.shuffle(worddata_dictionary)

# 3 second card flip timer
flip_id = window.after(3000, card_flip)

# show the first card
next_card()


canvas.bind("<Button-1>", print_coordinates)



window.mainloop()

