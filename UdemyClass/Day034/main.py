from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


api_parameters = {
    "amount": 10,
    "type": "boolean"
    }

# get questions from Open Trivia DB
response = requests.get("https://opentdb.com/api.php", params=api_parameters)
response.raise_for_status()
question_data = response.json()["results"]
#print(question_data)
print("Welcome to API Quiz Brain!\n\n")


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
