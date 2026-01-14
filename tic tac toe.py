from tkinter import *
from tkinter import messagebox
game_menu = Tk()
game_menu.geometry("600x700")
game_menu.config(bg="#1e293b")

turn = "X"
count = 0
win = False
winner = ""
buttons = []
global board

def multi_play():

    def check_game(but_num):
        global turn, count, win
        count = count + 1
        but_num.config(text = turn)
        but_num.config(state = DISABLED)

        if button1.cget("text") == button2.cget("text") == button3.cget("text") != "":
            result.config(text = "You win! " + turn)
            win = True
        if button4.cget("text") == button5.cget("text") == button6.cget("text") != "":
            result.config(text = "You win! " + turn)
            win = True
        if button7.cget("text") == button8.cget("text") == button9.cget("text") != "":
            result.config(text = "You win! " + turn)
            win = True
        if button1.cget("text") == button4.cget("text") == button7.cget("text") != "":
            result.config(text = "You win! " + turn)
            win = True
        if button2.cget("text") == button5.cget("text") == button8.cget("text") != "":
            result.config(text = "You win! " + turn)
            win = True
        if button3.cget("text") == button6.cget("text") == button9.cget("text") != "":
            result.config(text = "You win! " + turn)
            win = True
        if button1.cget("text") == button5.cget("text") == button9.cget("text") != "":
            result.config(text = "You win! " + turn)
            win = True
        if button3.cget("text") == button5.cget("text") == button7.cget("text") != "":
            result.config(text = "You win! " + turn)
            win = True

        if "X" == button1.cget("text") == button2.cget("text") == button3.cget("text") != "":
            winner = "X"
            messagebox.showinfo("Result","The winner is {}".format(winner))
        if "X" == button4.cget("text") == button5.cget("text") == button6.cget("text") != "":
            winner = "X"
            messagebox.showinfo("Result","The winner is {}".format(winner))
        if "X" == button7.cget("text") == button8.cget("text") == button9.cget("text") != "":
            winner = "X"
            messagebox.showinfo("Result","The winner is {}".format(winner))
        if "X" == button1.cget("text") == button5.cget("text") == button9.cget("text") != "":
            winner = "X"
            messagebox.showinfo("Result","The winner is {}".format(winner)) 
        if "X" == button3.cget("text") == button5.cget("text") == button7.cget("text") != "":
            winner = "X"
            messagebox.showinfo("Result","The winner is {}".format(winner)) 
        if "X" == button1.cget("text") == button4.cget("text") == button7.cget("text") != "":
            winner = "X"
            messagebox.showinfo("Result","The winner is {}".format(winner))  
        if "X" == button2.cget("text") == button5.cget("text") == button8.cget("text") != "":
            winner = "X"
            messagebox.showinfo("Result","The winner is {}".format(winner))
        if "X" == button3.cget("text") == button6.cget("text") == button9.cget("text") != "":
            winner = "X"
            messagebox.showinfo("Result","The winner is {}".format(winner))

        if "O" == button1.cget("text") == button2.cget("text") == button3.cget("text") != "":
            winner = "O"
            messagebox.showinfo("Result","The winner is {}".format(winner))
        if "O" == button4.cget("text") == button5.cget("text") == button6.cget("text") != "":
            winner = "O"
            messagebox.showinfo("Result","The winner is {}".format(winner))
        if "O" == button7.cget("text") == button8.cget("text") == button9.cget("text") != "":
            winner = "O"
            messagebox.showinfo("Result","The winner is {}".format(winner))
        if "O" == button1.cget("text") == button5.cget("text") == button9.cget("text") != "":
            winner = "O"
            messagebox.showinfo("Result","The winner is {}".format(winner)) 
        if "O" == button3.cget("text") == button5.cget("text") == button7.cget("text") != "":
            winner = "O"
            messagebox.showinfo("Result","The winner is {}".format(winner)) 
        if "O" == button1.cget("text") == button4.cget("text") == button7.cget("text") != "":
            winner = "O"
            messagebox.showinfo("Result","The winner is {}".format(winner))  
        if "O" == button2.cget("text") == button5.cget("text") == button8.cget("text") != "":
            winner = "O"
            messagebox.showinfo("Result","The winner is {}".format(winner))
        if "O" == button3.cget("text") == button6.cget("text") == button9.cget("text") != "":
            winner = "O"
            messagebox.showinfo("Result","The winner is {}".format(winner))

        if win == False and count == 9:
            result.config(text = "It is a tie!")
            messagebox.showinfo("Result","It is a tie!")

        if win == True:
            for button in buttons:
                button.config(state = DISABLED)

        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        turn_label.config(text = "Turn: {}".format(turn))

    multi_play_menu = Toplevel(game_menu)
    multi_play_menu.geometry("600x700")
    multi_play_menu.config(bg = "#1e293b")
    multi_play_menu.title("Multi Player")


    button1 = Button(multi_play_menu, text = "", font = ("Arial", 24),
                     command = lambda: check_game(button1))
    button1.place(x = 50, y = 80, width = 160, height = 160)

    button2 = Button(multi_play_menu, text = "", font = ("Arial", 24),
                     command = lambda: check_game(button2))
    button2.place(x = 220, y = 80, width = 160, height = 160)

    button3 = Button(multi_play_menu, text = "", font = ("Arial", 24),
                     command = lambda: check_game(button3))
    button3.place(x = 390, y = 80, width = 160, height = 160)

    button4 = Button(multi_play_menu, text = "", font = ("Arial", 24),
                     command = lambda: check_game(button4))
    button4.place(x = 50, y = 250, width = 160, height = 160)

    button5 = Button(multi_play_menu, text = "", font = ("Arial", 24),
                     command = lambda: check_game(button5))
    button5.place(x = 220, y = 250, width = 160, height = 160)

    button6 = Button(multi_play_menu, text = "", font = ("Arial", 24),
                     command=lambda: check_game(button6))
    button6.place(x = 390, y = 250, width = 160, height = 160)

    button7 = Button(multi_play_menu, text="", font=("Arial", 24),
                     command = lambda: check_game(button7))
    button7.place(x = 50, y = 420, width = 160, height = 160)

    button8 = Button(multi_play_menu, text = "", font = ("Arial", 24),
                     command = lambda: check_game(button8))
    button8.place(x = 220, y = 420, width = 160, height = 160)

    button9 = Button(multi_play_menu, text = "", font = ("Arial", 24),
                     command = lambda: check_game(button9))
    button9.place(x = 390, y = 420, width = 160, height = 160)

    buttons.extend([button1, button2, button3, button4, button5, button6, button7, button8, button9])



    result = Label(multi_play_menu,
                   text = "",
                   font = ("Comic Sans MS", 22),
                   width = 25,
                   height = 2,
                   bg = "gold")
    result.place(x = 80, y = 600)

    turn_label = Label(multi_play_menu,
                       text = "Turn: X",
                       font = ("Comic Sans MS", 20),
                       width = 15,
                       height = 1,
                       bg = "gold")
    turn_label.place(x = 180, y = 20)


welcome = Label(game_menu,
                text = "Welcome to Tic Tac Toe!",
                font = ("Comic Sans MS", 36),
                bg = "#334155",
                fg = "#facc15")
welcome.pack(pady = (60, 50))

single_player = Button(game_menu, text = "Single Player",
                       font = ("Comic Sans MS", 22),
                       bg = "#334155",
                       fg = "#e2e8f0",
                       width = 15,
                       height = 1)
single_player.pack(pady = 15)

multiplayer = Button(game_menu, text = "Multiplayer",
                     font = ("Comic Sans MS", 22),
                     bg = "#334155",
                     fg = "#e2e8f0",
                     width = 15,
                     height = 1,
                     command = multi_play)
multiplayer.pack(pady = 15)

leave = Button(game_menu, text = "Exit",
               font = ("Comic Sans MS", 22),
               bg = "#334155",
               fg = "#e2e8f0",
               width = 15,
               height = 1,
               command = game_menu.destroy)
leave.pack(pady = 15)

game_menu.mainloop()

