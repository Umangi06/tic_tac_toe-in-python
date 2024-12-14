import tkinter.messagebox
from tkinter import *
import os

def otic(root):
    root.destroy()
    os.system("three.py")

def ntic(root):
    root.destroy()
    os.system("four.py")

def utic(root):
    root.destroy()
    os.system("five.py")


root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background='Cadet Blue')

Tops = Frame(root, bg ='Cadet Blue', pady =2, width =1350,height=100, relief =RIDGE)
Tops.grid(row=0,column=0)

lblTitle =Label(Tops, font=('arial',70,'bold'), text="Tic Tac Toe", bd=21, bg='Cadet Blue',fg='Cornsilk', justify = CENTER)
lblTitle.grid(row=0,column=0)

btn1=Button(root, text="3 * 3",bd=21,font=('arial',10,'bold'), width=20,height=3,justify=CENTER,command=lambda:otic(root))
btn1.grid(row=3,column=3,padx=6,pady=11)

btn2=Button(root, text="4 * 4",bd=21,font=('arial',10,'bold'), width=20,height=3,justify=CENTER,command=lambda:ntic(root))
btn2.grid(row=4,column=3,padx=6,pady=13)

btn3=Button(root, text="5 * 5",bd=21,font=('arial',10,'bold'), width=20,height=3,justify=CENTER,command=lambda:utic(root))
btn3.grid(row=5,column=3,padx=6,pady=15)

root.mainloop()








