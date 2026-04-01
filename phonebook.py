from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("600x650")
window.config(bg = "light blue")
window.title("Phone Book")

def save_details():
    name = ename.get()
    mobile = emobile.get()
    result = "Name: " + name + ", Contact: " + mobile + "$a"
    file = open("phonebook.txt", "a")
    file.write(result)
    file.close()
    messagebox.showinfo("Info", "Information Saved!")

def fetch_details():
    file = open("phonebook.txt", "r")
    file_content = file.read()
    phone_list = file_content.split("$a")
    print(phone_list)
    l1.delete(0, END)
    for phone in phone_list:
            l1.insert(0, phone)

def show_details(event):
    w = event.widget
    selected_index = w.curselection()
    selected_item = w.get(selected_index[0])
    print(selected_item)
    details = selected_item.split(",")
    ename.delete(0, END)
    ename.insert(0, details[0])
    emobile.delete(0, END)
    emobile.insert(0, details[1])

book = Label(window, text = "Phone Book", font = ("Comic Sans MS", 26, "bold"), bg = "light blue")
book.place(x = 150, y = 20, width = 300)

op = Button(window, text = "Open", font = ("Comic Sans MS", 12), width = 12, command = fetch_details)
op.place(x = 240, y = 80)

l1 = Listbox(window, bg = "white")
l1.place(x = 50, y = 140, width = 220, height = 350)
l1.bind('<<ListboxSelect>>', show_details)

lname = Label(window, text = "Name:", font = ("Comic Sans MS", 12), bg = "light blue")
lname.place(x = 320, y = 160)

ename = Entry(window)
ename.place(x = 420, y = 160, width = 150)

lmobile = Label(window, text = "Contact:", font = ("Comic Sans MS", 12), bg = "light blue")
lmobile.place(x = 320, y = 230)

emobile = Entry(window)
emobile.place(x = 420, y = 230, width = 150)

update_add = Button(window, text = "Update/Add", width = 14, height = 2)
update_add.place(x = 100, y = 520)

save = Button(window, text = "Save", width = 14, height = 2, command = save_details)
save.place(x = 230, y = 520)

close = Button(window, text = "Close", width = 14, height = 2, command = window.destroy)
close.place(x = 360, y = 520)

window.mainloop()