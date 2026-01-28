from tkinter import *
import random
window = Tk()
window.title("Guess the number game")
window.geometry("400x250")

number = random.randint(1, 10)
player_name = ""

def save_name():
    global player_name
    player_name = name_entry.get()
    label1.config(text = "Hello {}".format(player_name) + "! Guess a number from 1-10")

def check_guess():
    guess = int(guess_entry.get())
    if guess == number:
        label1.config(text = "Correct! You win 🎉")
    elif guess >= number:
        label1.config(text = "Guess Lower!")  
    elif guess <= number:
        label1.config(text = "Guess Higher!")

label1 = Label(window, text = "Welcome to our game!")
label1.place(x = 120, y = 20)

label2 = Label(window, text = "What's your name?")
label2.place(x = 40, y = 60)

name_entry = Entry(window)
name_entry.place(x = 180, y = 60)

ok_button = Button(window, text = "OK", command = save_name)
ok_button.place(x = 180, y = 90)

guess_label = Label(window, text = "Take a guess:")
guess_label.place(x = 40, y = 130)

guess_entry = Entry(window)
guess_entry.place(x = 180, y = 130)

guess_button = Button(window, text = "Guess", command = check_guess)
guess_button.place(x = 180, y = 160)

window.mainloop()