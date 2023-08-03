from question_model import question_bank


class QuizBrain:
    def __init__(self, q_list, score):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def should_continue(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_view = input(f"{self.question_number}: {current_question.question_text} (true / false) ? ")
        return self.check_answer(user_view, current_question.answer.lower())

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
        print(f"Current Score: {self.score}")
