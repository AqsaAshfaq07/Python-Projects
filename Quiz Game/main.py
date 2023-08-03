from quiz_brain import QuizBrain
from question_model import question_bank, Question

print("The Brain Quiz ")
quiz = QuizBrain(question_bank, 0)

while quiz.should_continue():
    quiz.next_question()

print(f"Your Final score is {quiz.score} / {len(question_bank)}")
