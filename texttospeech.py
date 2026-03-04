from tkinter import *
import gtts
import os
window = Tk()
window.geometry("725x420")
window.configure(bg = "lightgreen")

def text_to_speech():
    text = text_entry.get()
    language = "en"
    speech = gtts.gTTS(text = text, lang = language, slow = False)
    speech.save("output.mp3")
    os.system("start output.mp3")

top_frame = Frame(window, bg = "pink", width = 725, height = 150)
top_frame.place(x = 0, y = 0)

title_label = Label(top_frame, text = "Text to Speech", bg = "pink", font = ("Arial", 28))
title_label.place(x = 230, y = 50)

text_entry = Entry(window, width = 40, font = ("Arial", 14))
text_entry.place(x = 150, y = 220)

submit_button = Button(window, text = "SUBMIT", bg = "yellow", font = ("Arial", 14), width = 12, command = text_to_speech)
submit_button.place(x = 290, y = 290)

window.mainloop()
