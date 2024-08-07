from question_model import QuestionCard
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# Loop through data
for question in question_data:
    new_question = QuestionCard(question["question"], question["correct_answer"])
    # print(f'{new_question.text} | {new_question.answer}')
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_q()

print(f"You've completed the quiz\n"
      f"Your final score was: {quiz.score}/{quiz.question_number}")