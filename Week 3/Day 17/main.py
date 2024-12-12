from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

new_quiz = Quiz_Brain(question_bank)
while new_quiz.still_has_questions():
    new_quiz.evaluate_Answer()
