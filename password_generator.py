from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

def copy_function():
    copypassword=pwdfield.get()
    pyperclip.copy(copypassword)

def showMessage():
    messagebox.showinfo("information","Password is being Successfully copied!")

def generate():
    small_alphabet=string.ascii_lowercase
    capital_alphabet=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabet+capital_alphabet+numbers+special_characters
    password_length=int(lengthbox.get())

    if var1.get()==1:
        pwdfield.insert(0,random.sample(small_alphabet,password_length))

    if var1.get()==2:
        pwdfield.insert(0,random.sample(small_alphabet+capital_alphabet,password_length))

    if var1.get()==3:
        pwdfield.insert(0,random.sample(all,password_length))

def reset():
    pwdfield.delete(0,'end')

win=Tk()
win.title("Password Generator")
win.geometry("430x600")
win.configure(bg="pink")
var1=IntVar()
heading=Label(win,text="Password Generator",font=("Times",35,"bold"),bg="pink",pady=10)
heading.grid()

weak=Radiobutton(win,text="Weak",value=1,variable=var1,font=("Times",25,"bold"),bg="pink")
weak.grid()

medium=Radiobutton(win,text="Medium",value=2,variable=var1,font=("Times",25,"bold"),bg="pink")
medium.grid()

strong=Radiobutton(win,text="Strong",value=3,variable=var1,font=("Times",25,"bold"),bg="pink")
strong.grid()

pwdlen=Label(win,text="Password Length",font=("Times",18,"bold"),bg="pink")
pwdlen.grid()

lengthbox=Spinbox(win,from_=5,to_=18,font=("Times",20,"bold"),width=8)
lengthbox.grid()

generateButton=Button(win,text="Generate",font=("Times",25,"bold"),bg="pink",command=generate)
generateButton.grid(pady=15)

pwdfield=Entry(win,width=20,font=("Times",25,"bold"))
pwdfield.grid()

resetButton=Button(win,text="Reset",font=("Times",18,"bold"),bg="pink",command=reset)
resetButton.grid(pady=5)

copy=Button(win,text="Copy",font=("Times",18,"bold"),bg="pink",command = lambda:[copy_function(),showMessage()])
copy.grid(pady=5)

win.mainloop()
