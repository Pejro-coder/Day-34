class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Method that prints all the questions and answers at the start:
    def quiz_list(self):
        for question in self.question_list:
            print(f"Nb:{self.question_list.index(question) + 1} {question.text} {question.answer}")

    def next_question(self):
        self.current_question = self.question_list[self.question_number]

        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def check_answer(self, choice):
        if self.question_number < len(self.question_list):
            if choice == self.question_list[self.question_number-1].answer:
                self.score += 1
                flash = "green"
            else:
                flash = "red"
            return flash
