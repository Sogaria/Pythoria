from question_model import Question
from data import question_api_data
from quiz_brain import Quiz_Brain
from ui import Ui_Interface

question_bank = []
for item in question_api_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

new_quiz = Quiz_Brain(question_bank)
ui_obj = Ui_Interface(new_quiz)

