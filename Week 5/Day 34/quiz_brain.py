from ui import Ui_Interface
class Quiz_Brain:

    def __init__(self, q_list: list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False