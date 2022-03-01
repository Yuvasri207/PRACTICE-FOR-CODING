from tkinter import *
import datetime
from tkinter.ttk import *
from tkinter.messagebox import *
import playsound

root=Tk()
root.title('ALARM CLOCK')
root.geometry("600x400")
def alarm():
    if c1.get()=="AM":
        x=int(e1.get())
        y=int(e2.get())
    if c1.get() == "PM":
        x = int(e1.get())+12
        y = int(e2.get())
    showinfo("notification", "alarm has been set")
    while True:
        if x == datetime.datetime.now().hour and y==datetime.datetime.now().minute:
            for i in range(0,100):
               playsound.Beep(10000,100)
            break
l1 = Label(root,text="hours:")
l2 = Label(root,text="minutes:")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1 = Button(root,text="set alarm",command=alarm)
b1.grid(row=2,column=1)
c1 = Combobox(root,values=["AM","PM"])
c1.grid(row=0,column=2)
l3 = Label(root,text="AM OR PM")
l3.grid(row=0,column=3)
root.mainloop()