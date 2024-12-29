from question_model import Question
from data import question_api_data
from quiz_brain import Quiz_Brain

question_bank = []
for item in question_api_data["results"]:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

new_quiz = Quiz_Brain(question_bank)
while new_quiz.still_has_questions():
    new_quiz.evaluate_Answer()

new_quiz.ending_screen()
