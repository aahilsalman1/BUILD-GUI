from tkinter import *
from tkinter import messagebox
import random
window = Tk()
window.geometry("600x400")
window.config(bg = "light blue")
window.title("Riddle Game!")

questions = ["What has a neck but no head?",
             "What has keys but no locks?",
             "What has to be broken before you can use it?",
             "What has hands but cannot clap?"]
answers = ["bottle", "piano", "egg", "clock"]

current_question = random.choice(questions)
i = questions.index(current_question)
current_answer = answers[i]
questions.remove(current_question)
answers.remove(current_answer)

def check_answer():
    global current_answer
    answer = enter.get()
    answer = answer.lower()
    if answer == current_answer:
        result.config(text = "Correct")
    else:
        result.config(text = "Incorrect")
        messagebox.showinfo("Wrong Answer", "Correct answer: " + current_answer)

def next_question():
    global questions, answers, current_question, current_answer
    current_question = random.choice(questions)
    i = questions.index(current_question)
    current_answer = answers[i]
    questions.remove(current_question)
    answers.remove(current_answer)
    enter.delete(0, END)
    question_label.config(text = current_question)
    result.config(text = "")

question_label = Label(window, text = current_question, font = ("Comic sans ms", 16),
                       bg = "light blue", wraplength = 500, justify = "center")
question_label.place(x = 50, y = 50, width = 500)

enter = Entry(window, width = 30, font = ("Arial", 12))
enter.place(x = 150, y = 150, width = 300)

result = Label(window, text = "", font = ("Arial", 12), bg = "light blue")
result.place(x = 250, y = 200)

sub = Button(window, text = "Submit", width = 15, height = 2, command = check_answer)
sub.place(x = 120, y = 260)

next = Button(window, text = "Next", width = 15, height = 2, command = next_question)
next.place(x = 320, y = 260)

window.mainloop()