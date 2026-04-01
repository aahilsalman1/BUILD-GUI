from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("700x750")
window.config(bg = "light blue")
window.title("Address Book")

def save_details():
    name = ename.get()
    mobile = emobile.get()
    email = eemail.get()
    address = eaddress.get("1.0", END)

    result = "Name: " + name + ", Mobile: " + mobile + ", Email: " + email + ", Address: " + address + "$a"

    file = open("addressbook.txt", "a")
    file.write(result)
    file.close()

    messagebox.showinfo("Info", "Information Saved!")

def fetch_details():
    file = open("addressbook.txt","r") 
    file_content = file.read()
    address_list = file_content.split("$a")
    print(address_list)
    for address in address_list:
        l1.insert(0,address)

def show_details(event):
    w = event.widget
    selected_index = w.curselection()
    selected_item = w.get(selected_index[0])
    print(selected_item)
    details = selected_item.split(",")
    ename.delete(0,END)
    ename.insert(0,details[0])
    emobile.delete(0,END)
    emobile.insert(0,details[1])
    eemail.delete(0,END)
    eemail.insert(0,details[2])
    eaddress.delete("1.0",END)
    eaddress.insert("1.0",details[3])

    

book = Label(window, text = "Address Book", font = ("Comic Sans MS", 26, "bold"), bg = "light blue")
book.place(x = 200, y = 20, width = 300)

op = Button(window, text = "Open", font = ("Comic Sans MS", 12), width = 12, command = fetch_details)
op.place(x = 290, y = 80)

l1 = Listbox(window, bg = "white")
l1.place(x = 50, y = 150, width = 250, height = 400)
l1.bind('<<ListboxSelect>>', show_details)

lname = Label(window, text = "Name:", font = ("Comic Sans MS", 12), bg = "light blue")
lname.place(x = 350, y = 160)

ename = Entry(window)
ename.place(x = 450, y = 160, width = 180)

lmobile = Label(window, text = "Contact:", font = ("Comic Sans MS", 12), bg = "light blue")
lmobile.place(x = 350, y = 220)

emobile = Entry(window)
emobile.place(x = 450, y = 220, width = 180)

lemail = Label(window, text = "Email:", font = ("Comic Sans MS", 12), bg = "light blue")
lemail.place(x = 350, y = 280)

eemail = Entry(window)
eemail.place(x = 450, y = 280, width = 180)

laddress = Label(window, text = "Address:", font = ("Comic Sans MS", 12), bg = "light blue")
laddress.place(x = 350, y = 340)

eaddress = Text(window)
eaddress.place(x = 450, y = 340, width = 180, height = 120)

update_add = Button(window, text = "Update/Add", width = 14, height = 2)
update_add.place(x = 120, y = 600)

save = Button(window, text = "Save", width = 14, height = 2, command = save_details)
save.place(x = 280, y = 600)

close = Button(window, text = "Close", width = 14, height = 2, command = window.destroy)
close.place(x = 440, y = 600)

window.mainloop()