class Quiz_Brain:

    def __init__(self, q_list: list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        if self.still_has_questions:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            return self.current_question.text
        else: 
            return None
    
    def evaluate_answer(self, answer: bool):
        correct_answer = self.current_question.answer == "True"
        if answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
            