import tkinter as tk
import string
import random

def password_generate():
    password = []
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
        passwords = " ".join(str(x)for x in password)
        label.config(text=passwords)

root = tk.Tk()
root.title('PASSWORD GENERATOR')
root.geometry("600x400")
button = tk.Button(root,text="Generate Password", command=password_generate)
button.grid(row=1, column=1)
label = tk.Label(root, font=("times", 15, "bold"))
label.grid(row=4, column=2)
root.mainloop()

