from tkinter import *
import datetime
window = Tk()
window.geometry("700x600")
window.title("Digital Clock")
window.configure(bg = "#1e1e2e")


def show_time():
    x = datetime.datetime.now()
    hours = x.strftime("%H")
    minutes = x.strftime("%M")
    seconds = x.strftime("%S")
    current_time = hours + ":" + minutes + ":" + seconds
    time_label.config(text = "The time is: " + str(current_time))
    time_label.after(1000, show_time)


def show_date():
    x = datetime.datetime.now()
    day = x.strftime("%d")
    month = x.strftime("%m")
    year = x.strftime("%Y")
    current_date = day + "/" + month + "/" + year
    date_label.config(text = "The date is: " + str(current_date))


label_clock = Label(
    window,
    text = "Digital Clock",
    font = ("Comic Sans MS", 20),
    bg = "#1e1e2e",
    fg = "white"
)
label_clock.place(x = 200, y = 30)


show_time_button = Button(
    window,
    text = "Show Time",
    width = 25,
    height = 2,
    bg = "#4CAF50",
    fg = "white",
    font = ("Comic Sans MS", 12),
    command = show_time
)
show_time_button.place(x = 200, y = 120)


time_label = Label(
    window,
    text = "",
    width = 30,
    height = 2,
    font = ("Comic Sans MS", 14),
    bg = "#2e2e3e",
    fg = "#00ffcc"
)
time_label.place(x = 180, y = 200)


show_date_button = Button(
    window,
    text = "Show Date",
    width = 25,
    height = 2,
    bg = "#2196F3",
    fg = "white",
    font = ("Comic Sans MS", 12),
    command = show_date
)
show_date_button.place(x = 200, y = 300)


date_label = Label(
    window,
    text = "",
    width = 30,
    height = 2,
    font = ("Comic Sans MS", 14),
    bg = "#2e2e3e",
    fg = "#ffcc00"
)
date_label.place(x = 180, y = 380)


window.mainloop()
