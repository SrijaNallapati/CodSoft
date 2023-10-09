from tkinter import *
from tkinter import messagebox

win=Tk()
win.title("ToDo")
win.geometry("400x330")
win.configure(bg="#00BFFF")

def add_task_func():
    task=entry_label.get()
    if task!="":
        list_box.insert(END,task)
        entry_label.delete(0,END)
    else:
        messagebox.showwarning("Warning!","You must enter a task!")

def delete_task_func():
    try:
        index=list_box.curselection()[0]
        list_box.delete(index)
    except:
        messagebox.showwarning("Warning!","You must select a task!")

def delete_all():
    list_box.delete(0,END)

heading=Label(win,text="To-Do Application",font=("Times",35,"bold"),bg="#00BFFF",pady=10)
heading.grid(padx=10)

list_box=Listbox(win,height=3,width=30,font=("Times",15,"bold"))
list_box.grid(padx=15)

entry_label=Entry(win,width=28,font=("Times",15,"bold"))
entry_label.grid(pady=10)

add_task=Button(win,width=25,text="Add Task",font=("Times",15,"bold"),bg="#00BFFF",command=add_task_func)
add_task.grid()

# save_task=Button(win,width=25,text="Save Task",font=("Times",15,"bold"),bg="#00BFFF",command=save_task_func)
# save_task.grid()

delete_task=Button(win,width=25,text="Delete Task",font=("Times",15,"bold"),bg="#00BFFF",command=delete_task_func)
delete_task.grid()

delete_all=Button(win,width=25,text="Delete All",font=("Times",15,"bold"),bg="#00BFFF",command=delete_all)
delete_all.grid()

win.mainloop()