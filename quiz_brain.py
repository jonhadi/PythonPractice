class QuizBrain:
    def __init__(self, quiz):
        self.question_list = quiz
        self.question_number = 0
        self.score = 0

    def next_q(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        student_a = input(f'Q.{self.question_number}:'
                          f' {current_question.text} (True/False)?: ')
        self.check_answer(student_a, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == "t":
            user_answer = "true"
        elif user_answer.lower() =="f":
            user_answer = "false"
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!\n"
                  f"The correct answer was: {correct_answer}\n"
                  f"You current score is: {self.score}/{self.question_number}\n")
        else:
            print(f"You got it wrong!\n"
                  f"The correct answer was: {correct_answer}\n"
                  f"You current score is: {self.score}/{self.question_number}\n")
