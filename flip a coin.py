from tkinter import messagebox
from tkinter import *
import random
window = Tk()
window.geometry("670x320")
window.config(bg = "light blue")
window.title("Flip a Coin!")


def play_game(user_choice):
    bot_choice = random.choice(["Heads", "Tails"])

    if bot_choice == user_choice:
        result = "Draw"
        messagebox.showinfo("Result:","Draw!")
    elif user_choice == "Heads":
        result = "Player wins"
        messagebox.showinfo("Result:","Player Wins!")     
    else:
        result = "Bot wins"
        messagebox.showinfo("Result:","Bot Wins!") 

    result_label.config(text = "Result: {}".format(result))


label1 = Label(window, text = "Flip the Coin!", font = ("Comic sans ms", 35))
label1.place(x = 100, y = 50)

label2 = Label(window, text = "Have a choice!", font = ("Comic sans ms", 20))
label2.place(x = 50, y = 150)

butt1 = Button(window, text = "Heads", font = ("Callibri", 10)
               ,width = 15, height = 2, bg = "green" ,command = lambda: play_game("Heads"))
butt1.place(x = 300, y = 150)

butt2 = Button(window, text = "Tails", font = ("Callibri", 10),
                width = 15, height = 2, bg = "blue",command = lambda: play_game("Tails"))
butt2.place(x = 450, y = 150)

result_label = Label(window, text = "", width = 15, height = 1, font = ("Comic sans ms", 20))
result_label.place(x = 100, y = 250)

def reset():
    result_label.config(text = "")

reset_butt = Button(window, text = "Reset", font = ("Callibri", 10), width = 10, height = 1, command = reset)
reset_butt.place(x = 400, y = 255)

window.mainloop()
