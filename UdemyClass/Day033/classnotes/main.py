from tkinter import *
import requests

quote_text = None
canvas = None


def get_quote():
    global quote_text
    global canvas
    
    kayne_quote = requests.get(url='https://api.kanye.rest')
    kayne_quote.raise_for_status()

    kayne_quote_text = kayne_quote.json()["quote"]
    canvas.itemconfig(quote_text, text=kayne_quote_text)
    #print(kayne_quote_text)
    
    


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()