class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Method that prints all the questions and answers at the start:
    def q_number_text_answers(self):
        for question in self.question_list:
            print(f"Nb:{self.question_list.index(question) + 1} {question.text} {question.answer}")

    def next_question(self):
        print(self.question_number)
        self.current_question = self.question_list[self.question_number]
        return f"Q.{self.question_number + 1}: {self.current_question.text}"
        # user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, choice):
        if choice == self.question_list[self.question_number].answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        self.question_number += 1  # TALE SHIT JE BIL PREJ POD next_question (zgoraj) in se je zato taled del:
        # choice == self.question_list[self.question_number].answer primerjal z naslednjim vprašanjem, ne s trenutnim
        if self.question_number < 10:
            print(f"Your current score is: {self.score}/{self.question_number}")
            print(f"Nb:{self.question_number + 1} {self.question_list[self.question_number].text} "
                  f"{self.question_list[self.question_number].answer}")
            print("")

    # def check_answer(self, user_answer):
    #     correct_answer = self.current_question.answer
    #     if user_answer.lower() == correct_answer.lower():
    #         self.score += 1
    #         print("You got it right!")
    #     else:
    #         print("That's wrong.")
    #
    #     print(f"Your current score is: {self.score}/{self.question_number}")
    #     print("\n")
