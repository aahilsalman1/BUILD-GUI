from tkinter import *
import random
window = Tk()
window.geometry("600x700")
window.config(bg = "light blue")
window.title("Riddle Game!")

questions = ["What has a neck but no head?"
             ,"What has keys but no locks?"
             ,"What has to be broken before you can use it?"
             ,"What has hands but cannot clap?"
             ]
answers = ["bottle","piano","egg","clock"]

current_question = random.choice(questions)
i =  questions.index(current_question)
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
        result.config(text  = "Incorrect")

def next_question():
    global questions, answers
    current_question = random.choice(questions)
    i =  questions.index(current_question)
    current_answer = answers[i]
    questions.remove(current_question)
    answers.remove(current_answer)
    enter.delete(0,END)
    question_label.config(text = current_question)
    result.config(text = "")

question_label = Label(window,text = current_question,font = ("Comic sans ms",16), 
                       width = 40, height = 1, bg = "light blue")
question_label.place(x = 50, y = 50)

enter = Entry(window, width = 20)
enter.place(x = 200, y = 150)

result = Label(window, width = 15, height = 1)
result.place(x = 200, y = 240)

sub = Button(window, text = "Submit", width = 20, height = 2, command = check_answer)
sub.place(x = 100, y = 320)

next = Button(window, text = "Next", width = 15, height = 2, command = next_question)
next.place(x = 300, y = 320)

window.mainloop()