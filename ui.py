from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

    # ------------------------------------ row 1 - Score label ------------------------------------
        self.score_label = Label(text=f"{self.quiz.score}/{self.quiz.question_number}", width=4, bg=THEME_COLOR,
                                 fg="white", font=("Arial", 20, "italic"))
        self.score_label.grid(column=1, row=0)

    # ------------------------------------ row 2 - QUOTE canvas ------------------------------------
        self.canvas = Canvas(width=300, height=200, highlightthickness=0, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=0, pady=60)
        self.question_text = self.canvas.create_text(150, 100,
                                                     width=280,
                                                     text="Hello, World!",
                                                     fill="black",
                                                     font=("Arial", 20, "italic"))

    # ------------------------------------row 3 - Buttons ------------------------------------
        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.choice_true)
        self.button_true.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.choice_false)
        self.button_false.grid(column=1, row=2)

    # ------------------------------------ get new question at the start, main loop ------------------------------------
        self.quiz.quiz_list()
        self.get_next_question()
        self.window.mainloop()

# --------------------- Next two functions take care of the red color flash, when the answer is wrong ------------------
    def change_to_white(self):
        # Change the background to white
        self.canvas.config(background="white")

    def flash_color(self, result):
        if result == "red":
            self.canvas.config(background="red")
            # Call another function to change the background to white after 1 second
            self.window.after(200, self.change_to_white)
        elif result == "green":
            self.canvas.config(background="green")
            # Call another function to change the background to white after 1 second
            self.window.after(200, self.change_to_white)

# ------------------------------------------ TRUE/FALSE buttons ------------------------------------------
    def get_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.window.after(4000, self.window.quit)

    def check_result_flash_color_update_score(self, choice):
        result = self.quiz.check_answer(choice)
        self.flash_color(result)
        self.score_label.config(text=f"{self.quiz.score}/{self.quiz.question_number}")

    # Function that takes care of what happens when the "true" button is pressed
    def choice_true(self):
        self.check_result_flash_color_update_score("True")
        self.get_next_question()

    # Function that takes care of what happens when the "false" button is pressed
    def choice_false(self):
        self.check_result_flash_color_update_score("False")
        self.get_next_question()
