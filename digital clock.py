from tkinter import *
import datetime
window = Tk()
window.geometry("700x600")
window.title("Digital Clock")
window.configure(bg = "Green")

def show_time():
    x = datetime.datetime.now()
    hours  = x.strftime("%H")
    minutes = x.strftime("%M")
    seconds = x.strftime("%S")
    current_time = hours + ":" + minutes + ":" + seconds
    time_label.config(text = "The time is:"+str(current_time))
    time_label.after(1000,show_time)

label_clock = Label(window, text = "Digital Clock:",width = 20, height = 2)
label_clock.place(x = 100, y = 20)

show_time_button = Button(window, text = "Show Time!", width = 30, height = 2, bg = "blue",
                           fg = "White", command = show_time)
show_time_button.place(x = 100, y = 120)

show_date_button = Button(window, text = "Show Date!", width = 30, height = 2, bg = "blue",
                           fg = "White")
show_date_button.place(x = 100, y = 320)

time_label = Label(window, text = "", width = 40, height = 2)
time_label.place(x = 100, y = 220)

date_label = Label(window, text = "", width = 40, height = 2)
date_label.place(x = 100, y = 420)

window.mainloop()