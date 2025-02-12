import tkinter

def button_clicked():
    km = 1.609344 * int(my_input.get())
    my_label2["text"] = str(round(km,1))



window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=10, pady=10)

my_input = tkinter.Entry(width=7)
my_input.grid(column=1,row=0)

my_label1 = tkinter.Label(text="Miles", font=("Arial", 14, "bold"), anchor="w")
my_label1.config(padx=10,pady=10)
my_label1.grid(column=2,row=0) 

my_label2 = tkinter.Label(text="0", font=("Arial", 14))
my_label2.grid(column=1,row=1) 

my_label3 = tkinter.Label(text="Kilometer", font=("Arial", 14, "bold"), anchor="w")
my_label3.config(padx=10,pady=10)
my_label3.grid(column=2,row=1) 

my_label4 = tkinter.Label(text="is equal to", font=("Arial", 12))
my_label4.config(padx=10,pady=10)
my_label4.grid(column=0,row=1) 

my_button = tkinter.Button(text="Convert", command=button_clicked)
my_button.grid(column=1,row=3)



window.mainloop()