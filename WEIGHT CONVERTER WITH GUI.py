from tkinter import *
window = Tk()
window.title('WEIGHT CONVERTER')
def from_kg():
    gram = float(user_value.get())*1000
    pound = float(user_value.get())*2.20462
    ounce = float(user_value.get())*35.274
    t1.delete('1.0', END)
    t1.insert(END, gram)
    t2.delete('1.0', END)
    t2.insert(END, pound)
    t3.delete('1.0', END)
    t3.insert(END, ounce)
e1 = Label(window,text='enter the weight in KG')
user_value = StringVar()
e2 = Entry(window,textvariable=user_value)
e3 = Label(window, text='gram')
e4 = Label(window, text='pound')
e5 = Label(window, text='ounce')

t1 = Text(window, height=2, width=30)
t2 = Text(window, height=2, width=30)
t3 = Text(window, height=2, width=30)

b1 = Button(window, text='convert', command=from_kg)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

window.mainloop()