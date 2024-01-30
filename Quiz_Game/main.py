# Importing modules
from question_model import Question
from question import question_data
from quiz_brain import QuizBrain
# Creating an empty question bank list
question_bank = []

# Iterating question data to get text and answer
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # Passing it in Question class and creating total instance
    total = Question(question_text, question_answer)
    # storing it in question_bank
    question_bank.append(total)

# Creating ques instance
ques = QuizBrain(question_bank)

# Using while loop to iterate until it is True
while ques.should_continue():
    ques.next_question()

# Printing the final score
print("--------------END OF QUIZ--------------")
print(f"Your Final Score : {ques.score}/{ques.question_number}")
print("---------------------------------------")