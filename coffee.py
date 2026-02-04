from tkinter import *
window = Tk()
window.geometry("700x600")
window.configure(bg = "light grey")
window.title("Coffee Generator!")

def calculate_price():
    selected_indices = box.curselection()
    if selected_indices:
        index = selected_indices[0]
        drink = box.get(index)

    sugars = sugar.get()
    milks = milk.get()
    print(drink, sugars, milks)
    bill = 0

    if drink == "Cappucino(£2.50)":
        bill = bill + 2.50
    elif drink == "Espresso(£3.00)":
        bill = bill + 3.00
    elif drink == "Machiato(£6.00)":
        bill = bill + 6.00
    elif drink == "Latte(£2.50)":
        bill = bill + 2.50
    elif drink == "Black Coffee(£3.50)":
        bill = bill + 3.50
    elif drink == "De-Caffe Latte(£2.50)":
        bill = bill + 2.50

    if sugars == "None":
        bill = bill + 0
    elif sugars == "Brown sugar":
        bill = bill + 0.50
    elif sugars == "White sugar":
        bill = bill + 0.50

    if milks == "Dairy milk":
        bill = bill + 1.20
    elif milks == "Soya milk":
        bill = bill + 0.80
    elif milks == "Almond milk":
        bill = bill + 0.99

    calculate.config(text = "Your total is: £" + str(bill) + "0")


drink_choice = Label(
    window,
    text = "Choose your drink:",
    font = ("Comic Sans MS", 14),
    bg = "light grey"
)
drink_choice.place(x = 50, y = 30)

items = [
    "Cappucino(£2.50)",
    "Espresso(£3.00)",
    "Machiato(£6.00)",
    "Latte(£2.50)",
    "Black Coffee(£3.50)",
    "De-Caffe Latte(£2.50)"
]

box = Listbox(
    window,
    height = 5,
    width = 30,
    bg = "white",
    fg = "blue"
)
box.place(x = 250, y = 30)

for i in range(len(items)):
    box.insert(i, items[i])

sugar_choice = Label(
    window,
    text = "Choose your sugar:",
    font = ("Comic Sans MS", 12),
    bg = "light grey"
)
sugar_choice.place(x = 50, y = 180)

sugar = StringVar()

sugar1 = Radiobutton(
    window,
    text = "None",
    value = "None",
    variable = sugar,
    bg = "light grey"
)
sugar1.place(x = 250, y = 180)

sugar2 = Radiobutton(
    window,
    text = "Brown sugar (£0.50)",
    value = "Brown sugar",
    variable = sugar,
    bg = "light grey"
)
sugar2.place(x = 320, y = 180)

sugar3 = Radiobutton(
    window,
    text = "White sugar (£0.50)",
    value = "White sugar",
    variable = sugar,
    bg = "light grey"
)
sugar3.place(x = 470, y = 180)

milk_choice = Label(
    window,
    text = "Choose your milk:",
    font = ("Comic Sans MS", 12),
    bg = "light grey"
)
milk_choice.place(x = 50, y = 250)

milk = StringVar()

milk1 = Radiobutton(
    window,
    text = "Dairy milk (£1.20)",
    value = "Dairy milk",
    variable = milk,
    bg = "light grey"
)
milk1.place(x = 250, y = 250)

milk2 = Radiobutton(
    window,
    text = "Soya milk (£0.80)",
    value = "Soya milk",
    variable = milk,
    bg = "light grey"
)
milk2.place(x = 380, y = 250)

milk3 = Radiobutton(
    window,
    text = "Almond milk (£0.99)",
    value = "Almond milk",
    variable = milk,
    bg = "light grey"
)
milk3.place(x = 520, y = 250)

brew = Button(
    window,
    text = "BREW",
    width = 20,
    height = 2,
    command = calculate_price
)
brew.place(x = 250, y = 330)

calculate = Label(
    window,
    text = "",
    font = ("Comic Sans MS", 12),
    bg = "light grey",
    width = 30,
    height = 2
)
calculate.place(x = 200, y = 400)

window.mainloop()
