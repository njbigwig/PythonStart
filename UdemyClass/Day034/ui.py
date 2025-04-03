import tkinter 
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        
        # program window frame with 20 pixel padding
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        
        # create canvas to attach items to
        self.canvas = tkinter.Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.question_text_id = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        
        self.score_label = tkinter.Label(text="Score: 0", font=("Arial", 14, "bold"), foreground="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1) 
        
        self.true_image = tkinter.PhotoImage(file="images\\true.png")
        self.true_button = tkinter.Button(command=self.button_click_true, highlightthickness=0, image=self.true_image )
        self.true_button.grid(row=2, column=0)
        
        self.false_image = tkinter.PhotoImage(file="images\\false.png")
        self.false_button = tkinter.Button(command=self.button_click_false, highlightthickness=0, image=self.false_image )
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text_id, text=q_text)
        
    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")               
    
    def restore_background_color(self):
        self.canvas.config(background="white")
        self.get_next_question()   
        
        if self.quiz.still_has_questions() == False:
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")
        
    def button_click_true(self):       
        print("TRUE Clicked")
    
        if self.quiz.check_answer("True"):
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")            
        self.window.after(1000, self.restore_background_color) 
        self.update_score()           
        
    def button_click_false(self):  
        print("FALSE Clicked")
        if self.quiz.check_answer("False"):
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")   
        self.window.after(1000, self.restore_background_color)          
        self.update_score()
        
        
        
    

