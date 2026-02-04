from tkinter import *
window = Tk()
window.geometry("800x700")
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

    if sugar == "None":
        bill = bill + 0
    elif sugar == "Brown Sugar(£0.50)":
        bill = bill + 0.50
    elif sugar == "White Sugar(£0.50)":
        bill = bill + 0.50

    if milk == "Dairy Milk(£1.20)":
        bill = bill + 1.20
    elif milk == "Soya Milk(£0.80)":
        bill = bill + 0.80
    elif milk == "Almond Milk(£0.99)":
        bill = bill + 0.99
    
    calculate.config(text = "Your total is: £"+str(bill))


drink_choice = Label(window, text = "Choose your drink:", font = ("Comic sans ms",15),
                     bg = "light grey", width = 15, height = 2 )
drink_choice.place(x = 50,y = 50)

items = ["Cappucino(£2.50)","Espresso(£3.00)","Machiato(£6.00)","Latte(£2.50)","Black Coffee(£3.50)","De-Caffe Latte(£2.50)"]

sc = Scrollbar(window)
sc.pack(side = RIGHT, fill = Y)

box = Listbox(window, height = 5, bg = "white",
               fg = "blue", activestyle = "dotbox", yscrollcommand = sc.set)
box.place(x = 300, y = 50)

for i in range(len(items)):
    box.insert(i,items[i])

sc.config()

sugar_choice = Label(window, text = "Choose your sugar:", font = ("Comic sans ms",10),
                     bg = "light grey", width = 15, height = 2 )
sugar_choice.place(x = 50,y = 150)

sugar = StringVar()

sugar1 = Radiobutton(window, text = "None", value = "None",
                     variable = sugar, bg = "light grey")
sugar1.place(x = 220, y = 150)

sugar2 = Radiobutton(window, text = "Brown sugar(£0.50)", value = "Brown sugar",
                     variable = sugar, bg = "light grey")
sugar2.place(x = 300, y = 150)

sugar3 = Radiobutton(window, text = "White sugar(£0.50)", value = "White sugar",
                     variable = sugar, bg = "light grey")
sugar3.place(x = 450, y = 150)

milk_choice = Label(window, text = "Choose your milk:", font = ("Comic sans ms",10),
                     bg = "light grey", width = 15, height = 2 )
milk_choice.place(x = 50,y = 250)

milk = StringVar()

milk1 = Radiobutton(window, text = "Dairy milk(£1.20)", value = "Dairy milk",
                     variable = milk, bg = "light grey")
milk1.place(x = 250, y = 250)

milk2 = Radiobutton(window, text = "Soya milk(£0.80)", value = "Soya milk",
                     variable = milk, bg = "light grey")
milk2.place(x = 360, y =250)

milk3 = Radiobutton(window, text = "Almond milk(£0.99)", value = "Almond milk",
                     variable = milk, bg = "light grey")
milk3.place(x = 500, y = 250)

brew = Button(window, text = "BREW" , bg = "light grey", height = 2, width = 25, command = calculate_price)
brew.place(x = 200, y = 350)

calculate = Label(window, text = "", font = ("Comic sans ms",10),
                     bg = "light grey", width = 15, height = 2 )
calculate.place(x = 200,y = 450)




window.mainloop()