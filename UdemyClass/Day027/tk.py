import tkinter
import time



# unlimited arguments - tuple
def add(*args):
    for n in args:
        print(n)
        
# Layout managers: 
# pack: place widgets below each other, starting at top, does not support good placement
# place: precise position, x & y value required
# grid: based on rows and columns

      
# event for button click
def button_clicked():
    print("I got clicked")
    my_label["text"] = my_input.get()         

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "Change label text"
my_label.config(text="New Text")
my_label.config(padx=10, pady=10)
#my_label.pack() # displays label on screen - has **kw advanced parameter
#my_label.place(x=10,y=10) # displays label on screen - has **kw advanced parameter
my_label.grid(column=0,row=0) # displays label on screen - has **kw advanced parameter
   

# add a button with an event processing function
my_button = tkinter.Button(text="Click Me", command=button_clicked)
#my_button.pack()
my_button.grid(column=1,row=1)

# add a second button
my_button2 = tkinter.Button(text="2nd Button", command=button_clicked)
#my_button.pack()
my_button2.grid(column=2,row=0)


# entry object = input
my_input = tkinter.Entry(width=10)
#my_input.pack()
my_input.grid(column=3,row=2)


# always at the end of the program
window.mainloop()



    
