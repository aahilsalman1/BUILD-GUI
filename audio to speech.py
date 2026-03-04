from tkinter import *
import speech_recognition as sr
window = Tk()
window.geometry("720x420")
window.title("Speech_notepad")

top_frame = Frame(window, bg = "pink", width = 725, height = 125)
top_frame.place(x = 0, y = 0)

title_label = Label(top_frame, text = "Voice Notepad", bg = "pink", font = ("Arial", 28))
title_label.place(x = 230, y = 50)

click_button = Button(window, text = "Click me to begin recording", bg = "yellow", font = ("Arial", 14),anchor = "s", width = 15, height = 3)
click_button.place(x = 20, y = 150)

window.mainloop()
