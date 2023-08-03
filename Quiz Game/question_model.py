from Questions_Data import question_data


class Question:
    def __init__(self, text, ans):
        self.question_text = text
        self.answer = ans


question_bank = [Question(question_data[i]["text"], question_data[i]["answer"]) for i in range(len(question_data))]
