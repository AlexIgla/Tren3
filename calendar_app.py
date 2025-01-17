from tkinter import *
import calendar
import datetime

root = Tk()
root.title("Calendar Example")
days = []
now = datetime.datetime.now()
year = now.year
month = now.month
# кнопка назад
back_button = Button(root, text="<")
back_button.grid(row=0, column=0, sticky=NSEW)
# кнопка вперед
next_button = Button(root, text=">")
next_button.grid(row=0, column=6, sticky=NSEW)
# настоящая дата
info_label = Label(root, text='0', width=1, height=1, font='Arial 16 bold', fg='blue')
info_label.grid(row=0, column=1, columnspan=5, sticky=NSEW)
# выводим дни недели
for n in range(7):
    lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1, font='Arial 10 bold', fg='darkblue')
    lbl.grid(row=1, column=n, sticky=NSEW)
    days.append(lbl)
# выводим строки календаря
for row in range(6):
    for col in range(7):
        lbl = Label(root, text='0', width=4, height=2, font='Arial 16 bold')
        lbl.grid(row=row + 2, column=col, sticky=NSEW)
        days.append(lbl)

root.mainloop()
