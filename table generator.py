from tkinter import *
window = Tk()
window.geometry("600x800")
window.config(bg = "light grey")
window.title("Times Table Generator!")

def generate_table():
    result = ""
    number = int(number_entry.get())
    r = range_choice.get()
    for i in range(r + 1):
        product = number * i
        result = result + str(number)+" x "+str(i)+" = "+str(product) + "\n" 
        label3.config(text = result)
        

label1 = Label(window, text = "Times Table Generator!", font = ("Comic sans ms",20))
label1.place(x = 100, y = 50)

label2 = Label(window, text = "Enter a number:", font = ("Comic sans ms",15))
label2.place(x = 50, y = 150)

number_entry = Entry(window, width = 20)
number_entry.place(x = 300, y = 150)

range_choice = IntVar()

range_label = Label(window, text = "Range", font = ("Comic sans ms",15))
range_label.place(x = 50, y = 220)

range1 = Radiobutton(window, text = 10, value = 10, variable = range_choice)
range1.place(x = 120, y = 220)

range2 = Radiobutton(window, text = 20, value = 20, variable = range_choice)
range2.place(x = 180, y = 220)

range3 = Radiobutton(window, text = 30, value = 30, variable = range_choice)
range3.place(x = 240, y = 220)

generate = Button(window, text = "Generate Table", font = ("Comic sans ms",15), width = 12, height = 2, command = generate_table)
generate.place(x = 100, y = 300)

label3 = Label(window, text = "Result:", font = ("Comic sans ms",8))
label3.place(x = 100, y = 400)


window.mainloop()