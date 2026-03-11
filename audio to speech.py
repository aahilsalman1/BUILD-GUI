from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
window = Tk()
window.title("Speech to Text")
window.geometry("1000x450")
window.config(bg = "light grey")

text = ""

def recognise_speech():
    global text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
        
    try:
        text = text+" "+r.recognize_google(audio)
        print(f"You said: {text}")
        text_box.insert(END,text)
    
    except Exception as e:
        print(f"Error: {e}")

def save_txt():
    global text
    file = open("output.txt","a")
    file.write(text)
    file.close()
    messagebox.showinfo("Info","Your text is saved!")
    

title = Label(window,
              text = "Voice Notepad",
              font = ("Arial", 32),
              bg = "light grey")
title.place(x = 310, y = 30)

record_btn = Button(window,
                    text = "Click on me!..\nTo start recording",
                    font = ("Arial", 14),
                    width = 20,
                    height = 3,
                    bg = "light grey",command = recognise_speech)
record_btn.place(x = 90, y = 180)

text_box = Text(window,
                width = 38,
                height = 3,
                font = ("Arial", 12))
text_box.place(x = 360, y = 190)

save_btn = Button(window,
                  text = "Save the Text",
                  font = ("Arial", 12),
                  width = 16,
                  height = 3,
                  bg = "light grey", command = save_txt)
save_btn.place(x = 720, y = 180)

window.mainloop()

