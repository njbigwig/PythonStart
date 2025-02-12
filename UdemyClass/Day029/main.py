import tkinter
from tkinter import messagebox
import os
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','^']

password_list = []

PASSWORDFILE = "pwd.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword_clicked():
    print("Generate Password Clicked")
    
    passwordstring = ""
    shufflepasswordstring = ""
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    # could have use list comprehension 3 times
    # password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    for pwdidx in range(0, nr_letters):
        passwordstring += random.choice(letters)

    for pwdidx in range(0, nr_symbols):
        passwordstring += random.choice(symbols)   
        
    for pwdidx in range(0, nr_numbers):
        passwordstring += random.choice(numbers)

    # this will create a scrambled list[]
    shufflepasswordlist = random.sample(passwordstring, len(passwordstring))
    
    # convert list to a string
    for pwdchar in shufflepasswordlist:
       shufflepasswordstring += pwdchar
    
    password_entry.delete(0, tkinter.END)   
    password_entry.insert(0, shufflepasswordstring)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_clicked():
    global password_list
    # open with "a" creates if there is no existing file
    print("Add button clicked")
    
    if len(website_entry.get()) == 0:
        messagebox.showwarning(title="Missing Entry", message="You need to enter in the website URL")
    elif len(username_entry.get()) == 0:
        messagebox.showwarning(title="Missing Entry", message="You need to enter in username")
    elif len(password_entry.get()) == 0:
        messagebox.showwarning(title="Missing Entry", message="You need to enter in your password")
    elif len(password_entry.get()) < 6:
        messagebox.showwarning(title="Entry Too Short", message="You need to enter in 6 or more password characters")
    else:
        #messagebox.showinfo(title="Password Save", message="Message")
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered:\nEmail: {username_entry.get()}\nPassword: {password_entry.get()}\n OK to save?")
    
        
        if is_ok == True:
            password_list = []
            if os.path.exists(PASSWORDFILE):
                print("Open existing password file")
                with open(PASSWORDFILE, "r") as pwdfile:
                    password_list = pwdfile.readlines()
                
                with open(PASSWORDFILE, "w") as pwdfile:
                    password_list.append(f"{username_entry.get()}|{password_entry.get()}|{website_entry.get()}\n")
                    pwdfile.writelines(password_list)     
            else:
                print("Creating password file")
                with open(PASSWORDFILE, "w") as pwdfile:
                    password_list.append(f"{username_entry.get()}|{password_entry.get()}|{website_entry.get()}\n")
                    pwdfile.writelines(password_list)
                    
            password_entry.delete(0, tkinter.END)
            website_entry.delete(0, tkinter.END)
            
            print(password_list)          


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
	
# Will use Tkinter Canvas
canvas =  tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
#canvas.pack()
canvas.grid(row=0, column=1)

# create labels
website_label = tkinter.Label(text="Website:", justify='right')
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:", justify='right')
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:", justify='right')
password_label.grid(row=3, column=0)

# create buttons
generatepassword_button = tkinter.Button(text="Generate Password", command=generatepassword_clicked, highlightthickness=0, bg="LightGray", justify='left')
generatepassword_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", command=add_clicked, highlightthickness=0, width=36, bg="LightGray")
add_button.grid(row=4, column=1, columnspan=2)

# create entry fields
website_entry = tkinter.Entry(width=35,  highlightthickness=0)
website_entry.insert(tkinter.END, string="")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = tkinter.Entry(width=35, highlightthickness=0)
username_entry.insert(0, string="dave@email.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = tkinter.Entry(width=21, highlightthickness=0, show="*")
password_entry.insert(tkinter.END, string="")
password_entry.grid(row=3, column=1)



window.mainloop()