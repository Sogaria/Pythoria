class Quiz_Brain:

    def __init__(self, q_list: list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def nextQuestion(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        prompt = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        return prompt

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def evaluate_Answer(self):
        correct_answer = self.question_list[self.question_number].answer
        if self.nextQuestion().lower() == correct_answer.lower():
            print("Correct Answer! :)")
            self.score += 1
            print(f"The correct answer was: {correct_answer}.")
            print(f"Current score: {self.score}/{self.question_number}.")
        else:
            print("Wrong Answer! :(")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Current score: {self.score}/{self.question_number}.")
        print()

    def ending_screen(self):
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}!")