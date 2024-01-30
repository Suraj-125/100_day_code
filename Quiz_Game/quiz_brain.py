# Creating QuzBrain class
class QuizBrain:
    def __init__(self, q_data):
        # Providing default value
        self.question_number = 0
        self.score = 0
        # Passing the list fo question
        self.question_list = q_data

    # Creating should_continue method
    def should_continue(self):
        # Checking is it True or False
        return self.question_number < len(self.question_list)

    # Creating next_question method
    def next_question(self):
        # Fetching the text from list
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Ques{self.question_number}: {current_question.text} True/False : ")
        self.check_answer(user_input, current_question.answer)

    # Creating check answer method
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right.")
            self.score += 1
        else:
            print("You are wrong.")
        print(f"Correct Answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")