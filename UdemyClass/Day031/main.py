import tkinter

BACKGROUND_COLOR = "#B1DDC6"

#my_image = PhotoImage(file="path/to/image_file.png")
#button = Button(image=my_image, highlightthickness=0)



def correct_guess():
    print("Correct Guess")   
    
def wrong_guess():
    print("Incorrect Guess")
    
def print_coordinates(event):
    x = event.x
    y = event.y
    print(f"Clicked at: x={x}, y={y}")
    

window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, width=900, height=626, background=BACKGROUND_COLOR)

canvas = tkinter.Canvas()
front_logo_image = tkinter.PhotoImage(file='images\\card_front.png')
image_id = canvas.create_image(526, 800, image=front_logo_image)
canvas.image = front_logo_image
canvas.grid(row=0, column=1, columnspan=2)

canvas2 = tkinter.Canvas()
back_logo_image = tkinter.PhotoImage(file='images\\card_back.png')
image_id2 = canvas2.create_image(526, 800, image=back_logo_image)
canvas2.image = back_logo_image
canvas2.grid(row=0, column=1, columnspan=2)





correct_image = tkinter.PhotoImage(file="images\\right.png")
correct_button = tkinter.Button(command=correct_guess, height=50, width=50, highlightthickness=0, image=correct_image)
correct_button.grid(row=1, column=2)

incorrect_image = tkinter.PhotoImage(file="images\\wrong.png")
incorrect_button = tkinter.Button(command=wrong_guess, height=50, width=50, highlightthickness=0, image=incorrect_image)
incorrect_button.grid(row=1, column=1)

language_label = tkinter.Label(text="French", font=("Arial", 40, "italic"))
language_label.place(x=114, y=45) 

word_label = tkinter.Label(text="trouve", font=("Arial", 60, "bold"))
word_label.place(x=80, y=125) 

canvas.bind("<Button-1>", print_coordinates)



window.mainloop()

