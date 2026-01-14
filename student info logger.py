from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Student information logger!")
window.geometry("720x300")
window.config(bg="#a8cf60")

percentage = 0
grade = ""

def calc_percentage():
    global percentage

    name = name_entry.get()
    roll_num = roll_num_entry.get()

    if (name == "" or roll_num == ""):
        messagebox.showinfo("Error!","Please enter Name and RollNumber first.")
    
    else:
        science = int(science_entry.get())
        maths = int(maths_entry.get())
        english = int(english_entry.get())
        history = int(history_entry.get())
        geography = int(geography_entry.get())

        total = science + maths + english + history + geography
        percentage = (total/500)*100
    
        gr_pe.config(text = "Your percentage is {}".format(percentage))

def calc_grade():
    global percentage, grade

    if percentage == 0:
        messagebox.showinfo("Error!","Please calculate percentage before calculating grade.")    

    else:
        if percentage >= 80:
            grade = "A"
        elif percentage >= 70 and percentage < 80:
            grade = "B"
        elif percentage >= 60 and percentage < 70:
            grade = "C"
        elif percentage >= 50 and percentage < 60:
            grade = "D"
        else:
            grade = "F"
    
        gr_pe.config(text = "Your grade is {}".format(grade))

def save_report():
    global percentage, grade

    if percentage == 0:
        messagebox.showinfo("Error","Please enter a value for the percentage.")

    else:
        name = name_entry.get()
        roll_num = roll_num_entry.get()
        file = open("student.txt","a")
        file.write("Name: {} , RollNumber: {} , Percentage: {} , Grade: {}".format(name,roll_num,percentage,grade))
        file.write("\n")
        file.close()

        messagebox.showinfo("Success!","Your details are saved!")

main_frame = Frame(window, bg  ="white")
main_frame.place(x = 10, y = 10, width = 700, height = 280)

title = Label(main_frame, text = "STUDENT REPORT LOG", bg = "white", font = ("Comic sans ms", 10))
title.place(x = 20, y = 10)

name = Label(main_frame, text = "Name:", bg = "white")
name.place(x = 20, y = 40)
name_entry = Entry(main_frame, width = 25)
name_entry.place(x=100, y=40)

roll_num = Label(main_frame, text = "RollNumber :", bg = "white")
roll_num.place(x = 20, y = 70)
roll_num_entry = Entry(main_frame, width = 25)
roll_num_entry.place(x=100, y=70)

science = Label(main_frame, text = "Science:", bg = "white")
science.place(x = 360, y = 40)
science_entry = Entry(main_frame, width = 25)
science_entry.place(x = 500, y = 40)

maths = Label(main_frame, text = "Math :", bg = "white")
maths.place(x = 360, y = 70)
maths_entry = Entry(main_frame, width = 25)
maths_entry.place(x = 500, y = 70)

english = Label(main_frame, text = "English:", bg = "white")
english.place(x = 360, y = 100)
english_entry = Entry(main_frame, width = 25)
english_entry.place(x = 500, y = 100)

history = Label(main_frame, text = "History:", bg = "white")
history.place(x = 360, y = 130)
history_entry = Entry(main_frame, width = 25)
history_entry.place(x = 500, y = 130)

geography = Label(main_frame, text = "Geography:", bg = "white")
geography.place(x = 360, y = 160)
geography_entry = Entry(main_frame, width = 25)
geography_entry.place(x = 500, y = 160)

calculate_percentage = Button(main_frame, text = "Percentage", width = 10, command = calc_percentage)
calculate_percentage.place(x = 20, y = 220)

calculate_grade = Button(main_frame, text = "Grade", width = 10, command = calc_grade)
calculate_grade.place(x = 130, y = 220)

save = Button(main_frame, text = "Save", width = 10, command = save_report)
save.place(x = 220, y = 220)

gr_pe = Label(main_frame, text = "", height = 2, width = 30)
gr_pe.place(x = 350, y = 220)

window.mainloop()
