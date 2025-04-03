import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q_text = None
        if self.question_number == 10:
            q_text = f"Quiz Complete!"
        else:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"            
        return q_text
        #user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        #self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        answer_check = False
        
        if user_answer.lower() == correct_answer.lower():
            if self.question_number < 10:
                self.score += 1
            answer_check = True
        
        return answer_check
            #print("You got it right!")
        #else:
        #    print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
