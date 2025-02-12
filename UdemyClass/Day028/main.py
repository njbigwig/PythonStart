import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # was 25
SHORT_BREAK_MIN = 5 # was 5
LONG_BREAK_MIN = 20 # was 20

work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60

reps = 0

timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked():
    global reps
    
    reps += 1
    
    if reps <= 8:
        
        print(f"Start Clicked Reps: {reps}")
    
        # 1st rep = 25 min work
        # 2nd rep = 5 min break
        # 3rd rep = 25 min work
        # 4th rep = 5 min break
        # 5th rep = 25 min work
        # 6th rep = 5 min break
        # 7th rep = 25 min work
        # 8th rep = 20 min break 
    
     
        if reps % 2 == 0 and reps != 8:
            phase_label["text"] = "Break"
            phase_label["fg"] = PINK
            rounds_label["text"] = "✔"*int(reps/2)
            # cound use phase_label.config(text="blah", fg=GREEN)
            count_down(short_break_sec)
        elif reps % 2 != 0 and reps != 8:
            phase_label["text"] = "Work"
            phase_label["fg"] = GREEN            
            count_down(work_sec)
        elif reps == 8:
            phase_label["text"] = "Break"
            phase_label["fg"] = RED
            rounds_label["text"] = "✔"*int(reps/2)
            count_down(long_break_sec)      
    
       # 5 minutes = count_down(5*60), start with 25 minutes of work
  
    
def reset_clicked():
    global reps
    
    print("Reset Clicked")
    window.after_cancel(timer)
    reps = 0
    rounds_label["text"] = " "
    phase_label["text"] = " "
    canvas.itemconfig(timer_text, text=" ")
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def say_something(a, b, c):
    print(a)
    print(b)
    print(c)
    
def count_down(count): 
    global reps
    global timer
    
    # count -= 10 # speed up for debugging
    print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        print("Timer Completed")
        if reps > 0:
            start_clicked()    

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.iconbitmap("tomato.ico")

	
# Will use Tkinter Canvas
canvas =  tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

# setup timer event
#window.after(ms=5000, func=lambda: say_something(3, 5, 8))
#count_down(5)

rounds_label = tkinter.Label(text=" ", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
rounds_label.place(x=30, y=235)

phase_label = tkinter.Label(text="Task", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
phase_label.place(x=40, y=-40)

start_button = tkinter.Button(text="Start", command=start_clicked, bg=PINK, highlightthickness=0)
start_button.place(x=-10, y=220)

reset_button = tkinter.Button(text="Reset", command=reset_clicked, bg=PINK, highlightthickness=0)
reset_button.place(x=160, y=220)




window.mainloop()