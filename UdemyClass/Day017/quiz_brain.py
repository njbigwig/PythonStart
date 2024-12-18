
# could have put in the torf.py input() call in next_question() method

class QuizBrain:
    def __init__(self, questions):
        self.questionnumber = 0
        self.score = 0
        self.questionlist = questions
    def next_question(self): # Method
        if len(self.questionlist) > 0:
            self.questionnumber += 1
            return self.questionlist.pop(0)
        else:
            return None
    def still_has_questions(self):
        if len(self.questionlist) > 0:
            return True
        else:
            return False 
    def check_answer(self, user_text, answer_text):
        if user_text.lower() == answer_text.lower():
            self.score += 1
            print(f"Correct! Your score = ({self.score}/{self.questionnumber})\n")
            return True
        else:
            print(f"Wrong, correct answer = {answer_text}. Your score = ({self.score}/{self.questionnumber})\n")
            return False
    def show_score(self):
        score_val = (self.score/self.questionnumber) * 100
        print(f"Score: {score_val:.1f}%")
