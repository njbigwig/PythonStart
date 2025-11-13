from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter
from tkinter import filedialog
import re

pressure_timer = 30

def resettimer():
    global pressure_timer
    global label
    global entry
    global window
   
    label.config(text="30")
    word_text.config(text="Word Count: 0")
    entry.delete("1.0", tkinter.END)
    pressure_timer = 30
    window.after(1000, process_timer)    
    
    
def process_timer():
    global pressure_timer
    global label
    global entry
    global window
    
    if len(entry.get("1.0", tkinter.END).strip()) > 0:
        if pressure_timer > 0:
            pressure_timer -= 1
        
            label.config(text=f"{pressure_timer}")
            
            window.after(1000, process_timer)
        elif pressure_timer == 0:
            entry.delete("1.0", tkinter.END)
            entry.insert("1.0", "You took too long, reset and try again....")
    
    else:
        window.after(1000, process_timer)
        
        

def key_press(event):
    global pressure_timer
    global label
    global entry
    global word_text
    
    print(f"Keyboard Entry: {event.char} Len = {len(entry.get("1.0", tkinter.END).strip())}")
    label.config(text="30")
    pressure_timer = 30
    
    text = entry.get("1.0", "end-1c")  # Get text without trailing newline
    words = re.findall(r'\b\w+\b', text)  # Match words separated by space or punctuation
    word_text.config(text=f"Word Count: {len(words)}")
    print(f"Word count: {len(words)}")
    

#Creating a new window and configurations
window = tkinter.Tk()
window.title("Editor with Pressure")
window.minsize(width=500, height=500)

# bind keyboard character input
window.bind("<Key>", key_press)

label = tkinter.Label(text="30")
label.place(x=450,y=10)

word_text = tkinter.Label(text="Word Count: 0")
word_text.place(x=150,y=150)

# Entry Field
entry = tkinter.Text(window, width=50, height=5)
entry.delete("1.0", tkinter.END)
entry.place(x=5,y=30)
#print(entry.get())
# user_input = text_box.get("1.0", tk.END).strip()

# calls action() when pressed
button = tkinter.Button(text="Reset", command=resettimer)
button.place(x=450,y=450)

process_timer()

window.mainloop()