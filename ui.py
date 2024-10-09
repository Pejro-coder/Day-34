from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("yolo")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # row 1 - Score label
        self.score_label = Label(text=f"{self.quiz.score}/{self.quiz.question_number}", width=15, bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # row 2 - QUOTE canvas
        self.canvas = Canvas(width=300, height=200, highlightthickness=0, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=0, pady=60)
        self.question_text = self.canvas.create_text(150, 100,
                                                     width=280,
                                                     text="Hello, World!",
                                                     fill="black",
                                                     font=("Arial", 20, "italic"))

        # row 3 - Buttons
        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.choice_true)
        self.button_true.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.choice_false)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()
        self.quiz.q_number_text_answers()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)

    def choice_true(self):
        if self.quiz.question_number == 9:
            self.quiz.check_answer("True")  # I thought the "True" was boolean, but it was string...
            self.score_label.config(text=f"{self.quiz.score}/{self.quiz.question_number}")
            self.window.quit()
        else:
            self.quiz.check_answer("True")  # I thought the "True" was boolean, but it was string...
            self.score_label.config(text=f"{self.quiz.score}/{self.quiz.question_number}")
            self.get_next_question()

    def choice_false(self):
        if self.quiz.question_number == 9:
            self.quiz.check_answer("False")
            self.score_label.config(text=f"{self.quiz.score}/{self.quiz.question_number}")
            self.window.quit()
        else:
            self.quiz.check_answer("False")
            self.score_label.config(text=f"{self.quiz.score}/{self.quiz.question_number}")
            self.get_next_question()
        # self.score_label.config(text=f"{self.quiz.score}/{self.quiz.question_number}")
