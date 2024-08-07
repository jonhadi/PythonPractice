from question_model import QuestionCard
from data import question_data

question_bank = []
question_cu = []
# Loop through data
for position in range(0, len(question_data) - 1):
    new_question = QuestionCard(question_data[position])
    question_bank.append(new_question)
print(question_bank[0].answer)

for question in question_data:
    new_question = question
    question_cu.append(new_question)