THEME_COLOR = "#375362"
from tkinter import *


class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.language_text = self.canvas.create_text(150, 125, text="French", font=("Ariel", 40, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, foreground="white")
        self.score.grid(column=1, row=0 )



        self.window.mainloop()