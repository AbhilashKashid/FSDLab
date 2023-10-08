from tkinter import *
import calendar

window = Tk()
window.geometry('400x300')
window.title('Calender')

def show():
    m = int(month.get())
    y = int(year.get())
    output = calendar.month(y, m)
    cal.insert('end', output)

def clear():
    cal.delete(1.0, 'end')

def exit():
    window.destroy()

month_label = Label(window, text="Month", font=('verdana', '10', 'bold'))
month_label.place(x=50, y=40)
month = Spinbox(window, from_=1, to=12, width=5)
month.place(x=120, y=40)
year_label = Label(window, text="Year", font=('verdana', '10', 'bold'))
year_label.place(x=210, y=40)
year = Spinbox(window, from_=2020, to=3000, width=8)
year.place(x=260, y=40)
cal = Text(window, width=30, height=8, relief=RIDGE, borderwidth=2)
cal.place(x=70, y=110)
show = Button(window, text="Show", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=show)
show.place(x=100, y=250)
clear = Button(window, text="Clear", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=clear)
clear.place(x=160, y=250)
exit = Button(window, text="Exit", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=exit)
exit.place(x=220, y=250)
window.mainloop()
