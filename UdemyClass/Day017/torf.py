import data
import question_model
import quiz_brain

question_bank = []

# create a list of Question objects using question_data dictionaries
print("Generating question bank...\n")
for question in data.question_data:
    question_bank.append(question_model.Question(question['text'], question['answer'], False))
    
#print(f"Question Bank Size: {len(question_bank)}")
#print(question_bank)
#print(question_bank[0].text, question_bank[0].answer)

quiz_brain = quiz_brain.QuizBrain(question_bank)


while quiz_brain.still_has_questions() == True:
    question = quiz_brain.next_question()
    if question != None:
        answer_input = input(f"Q.{quiz_brain.questionnumber} {question.text} (True/False): ")
        #print(question.text, question.answer)
        quiz_brain.check_answer(answer_input,question.answer)

print("You have completed the quiz!")
quiz_brain.show_score()          
    

    
