from tkinter import *
win=Tk()
win.geometry("318x400")
win.title("Calculator")
win.config(bg="black")

equation=StringVar()
equation.set("")

expression=""

def calculate(num):
    global expression
    expression = expression +str(num)
    equation.set(expression)

def clear():
    global expression
    expression=""
    equation.set("")

def result():
    global expression
    total=str(eval(expression))
    equation.set(total)
    expression=""

Result=Entry(win,textvariable=equation,width=13,font=("Times",30,"bold"))
Result.grid(pady=25,padx=13,ipadx=15,ipady=15)

frame1=Frame(win,bg="black")
B1=Button(frame1,text="7",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(7))
B1.grid(row=0,column=0,pady=1,padx=1)
B2=Button(frame1,text="8",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(8))
B2.grid(row=0,column=1,pady=1,padx=1)
B3=Button(frame1,text="9",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(9))
B3.grid(row=0,column=2,pady=1,padx=1)
B4=Button(frame1,text="/",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate("/"))
B4.grid(row=0,column=3,pady=1,padx=1)
frame1.grid(padx=10)

frame2=Frame(win,bg="black")
B5=Button(frame2,text="4",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(4))
B5.grid(row=1,column=0,pady=1,padx=1)
B6=Button(frame2,text="5",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(5))
B6.grid(row=1,column=1,pady=1,padx=1)
B7=Button(frame2,text="6",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(6))
B7.grid(row=1,column=2,pady=1,padx=1)
B8=Button(frame2,text="x",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate("*"))
B8.grid(row=1,column=3,pady=1,padx=1)
frame2.grid(padx=10)

frame3=Frame(win,bg="black")
B9=Button(frame3,text="1",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(1))
B9.grid(row=2,column=0,pady=1,padx=1)
B10=Button(frame3,text="2",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(2))
B10.grid(row=2,column=1,pady=1,padx=1)
B11=Button(frame3,text="3",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(3))
B11.grid(row=2,column=2,pady=1,padx=1)
B12=Button(frame3,text="-",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate("-"))
B12.grid(row=2,column=3,pady=1,padx=1)
frame3.grid(padx=10)

frame4=Frame(win,bg="black")
B13=Button(frame4,text="C",font=("Times",15,"bold"),width=5,height=2,bg="red",fg="white",command=clear)
B13.grid(row=3,column=0,pady=1,padx=1)
B14=Button(frame4,text="0",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate(0))
B14.grid(row=3,column=1,pady=1,padx=1)
B15=Button(frame4,text="=",font=("Times",15,"bold"),bg="green",fg="white",width=5,height=2,command=result)
B15.grid(row=3,column=2,pady=1,padx=1)
B16=Button(frame4,text="+",font=("Times",15,"bold"),width=5,height=2,command=lambda : calculate("+"))
B16.grid(row=3,column=3,pady=1,padx=1)
frame4.grid(padx=10)


win.mainloop()