class Question:
    def __init__(self, question_text, question_answer, db):
        self.text =  question_text
        self.answer = question_answer
        if db == True:
            print(f"New Q: {self.text} = {self.answer}")
