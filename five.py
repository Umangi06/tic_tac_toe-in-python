import tkinter.messagebox
from tkinter import*

#create the root
root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background='Cadet Blue')

def utic(root):
    root.destroy()
    import level

Tops = Frame(root, bg ='Cadet Blue', pady =2, width =1350,height=100, relief =RIDGE)
Tops.grid(row=0,column=0)

Button(Tops, text="Back",bd=21, width=20,command=lambda:utic(root)).grid(row=0,column=1)


lblTitle =Label(Tops, font=('arial',50,'bold'), text="Tic Tac Toe", bd=21, bg='Cadet Blue',fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame (root, bg ='Powder Blue', pady=2, width =1350,height=600, relief =RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame (MainFrame, bd=10, width =550,height=500, pady=2, padx=10, bg ='Powder Blue', relief =RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame (MainFrame, bd=10, width =450,height=500, padx=10, pady=2, bg ='Powder Blue', relief =RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame (RightFrame, bd=10, width =200,height=200, padx=10, pady=2, bg ='Powder Blue', relief =RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame (RightFrame, bd=10, width =200,height=200, padx=10, pady=2, bg ='Powder Blue', relief =RIDGE)
RightFrame2.grid(row=1, column=0)

PlayerX=IntVar()
PlayerO=IntVar()
                                                                    
PlayerX.set(0)
PlayerO.set(0)

btn_click= StringVar()
click = True


#create btn_click funnction
def btn_click(btn_clicked):
    btn_clicked['text']='X'
    #btn_clicked['state']='disabled'
    btn_clicked['bg']='gainsboro'

    def checkforwinner():
        #if first row is X
        if b1['text'] == 'X' and b2['text'] == 'X'and b3['text'] == 'X' and b4['text'] == 'X' and b5['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b6['text'] == 'X' and b7['text'] == 'X'and b8['text'] == 'X' and b9['text'] == 'X' and b10['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b11['text'] == 'X' and b12['text'] == 'X'and b13['text'] == 'X' and b14['text'] == 'X' and b15['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b16['text'] == 'X' and b17['text'] == 'X'and b18['text'] == 'X' and b19['text'] == 'X' and b20['text'] == 'X':
            #make all btn disable
            #for btn in buttons:
                #btn['state']='disabled'
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b21['text'] == 'X' and b22['text'] == 'X'and b23['text'] == 'X' and b24['text'] == 'X' and b25['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b1['text'] == 'X' and b6['text'] == 'X'and b11['text'] == 'X' and b16['text'] == 'X' and b21['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b2['text'] == 'X' and b7['text'] == 'X'and b12['text'] == 'X' and b17['text'] == 'X' and b22['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b3['text'] == 'X' and b8['text'] == 'X'and b13['text'] == 'X' and b18['text'] == 'X' and b23['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b4['text'] == 'X' and b9['text'] == 'X'and b14['text'] == 'X' and b19['text'] == 'X' and b24['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b5['text'] == 'X' and b10['text'] == 'X'and b15['text'] == 'X' and b20['text'] == 'X' and b25['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b1['text'] == 'X' and b7['text'] == 'X'and b13['text'] == 'X' and b19['text'] == 'X' and b25['text'] == 'X':
            #make all btn disable
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")

        elif b5['text'] == 'X' and b9['text'] == 'X'and b13['text'] == 'X' and b17['text'] == 'X' and b21['text'] == 'X':
            #make all btn disable
            #for btn in buttons:
                #btn['state']='disabled'
            n=float(PlayerX.get())
            score=(n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","You have just won a game")
            
        else:
            emptybuttons = []
            if b1['text'] == "":
                emptybuttons.append(b1)
            if b2['text'] == "":
                emptybuttons.append(b2)
            if b3['text'] == "":
                emptybuttons.append(b3)
            if b4['text'] == "":
                emptybuttons.append(b4)
            if b5['text'] == "":
                emptybuttons.append(b5)
            if b6['text'] == "":
                emptybuttons.append(b6)
            if b7['text'] == "":
                emptybuttons.append(b7)
            if b8['text'] == "":
                emptybuttons.append(b8)
            if b9['text'] == "":
                emptybuttons.append(b9)
            if b10['text'] == "":
                emptybuttons.append(b10)
            if b11['text'] == "":
                emptybuttons.append(b11)
            if b12['text'] == "":
                emptybuttons.append(b12)
            if b13['text'] == "":
                emptybuttons.append(b13)
            if b14['text'] == "":
                emptybuttons.append(b14)
            if b15['text'] == "":
                emptybuttons.append(b15)
            if b16['text'] == "":
                emptybuttons.append(b16)
            if b17['text'] == "":
                emptybuttons.append(b17)
            if b18['text'] == "":
                emptybuttons.append(b18)
            if b19['text'] == "":
                emptybuttons.append(b19)
            if b20['text'] == "":
                emptybuttons.append(b20)
            if b21['text'] == "":
                emptybuttons.append(b21)
            if b22['text'] == "":
                emptybuttons.append(b22)
            if b23['text'] == "":
                emptybuttons.append(b23)
            if b24['text'] == "":
                emptybuttons.append(b24)
            if b25['text'] == "":
                emptybuttons.append(b25)

        #randomly select a btn
            import random
            random_button=random.choice(emptybuttons)

        #change btn text to O
            random_button.config(text="O")

        #make btn disable
            random_button.config(bg="Cadet Blue")

        #clear the list
            emptybuttons.clear()


        if b1['text'] == 'O' and b2['text'] == 'O'and b3['text'] == 'O' and b4['text'] == 'O' and b5['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b6['text'] == 'O' and b7['text'] == 'O'and b8['text'] == 'O' and b9['text'] == 'O' and b10['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b11['text'] == 'O' and b12['text'] == 'O'and b13['text'] == 'O' and b14['text'] == 'O' and b15['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b16['text'] == 'O' and b17['text'] == 'O'and b18['text'] == 'O' and b19['text'] == 'O' and b20['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b21['text'] == 'O' and b22['text'] == 'O'and b23['text'] == 'O' and b24['text'] == 'O' and b25['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

                
        elif b1['text'] == 'O' and b6['text'] == 'O'and b11['text'] == 'O' and b16['text'] == 'O' and b21['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b2['text'] == 'O' and b7['text'] == 'O'and b12['text'] == 'O' and b17['text'] == 'O' and b22['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b3['text'] == 'O' and b8['text'] == 'O'and b13['text'] == 'O' and b18['text'] == 'O' and b23['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b4['text'] == 'O' and b9['text'] == 'O'and b14['text'] == 'O' and b19['text'] == 'O' and b24['text'] == 'O':
            #make all btn disable
            #for btn in buttons:
                #btn['state']='disabled'
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b5['text'] == 'O' and b10['text'] == 'O'and b15['text'] == 'O' and b20['text'] == 'O' and b25['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")

        elif b1['text'] == 'O' and b7['text'] == 'O'and b13['text'] == 'O' and b19['text'] == 'O' and b25['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")
            
        elif b5['text'] == 'O' and b9['text'] == 'O'and b13['text'] == 'O' and b17['text'] == 'O' and b21['text'] == 'O':
            #make all btn disable
            n=float(PlayerO.get())
            score=(n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","Device have just won a game")
            
    checkforwinner()

def reset():
    b1["text"]=""
    b2["text"]=""
    b3["text"]=""
    b4["text"]=""
    b5["text"]=""
    b6["text"]=""
    b7["text"]=""
    b8["text"]=""
    b9["text"]=""
    b10["text"]=""
    b11["text"]=""
    b12["text"]=""
    b13["text"]=""
    b14["text"]=""
    b15["text"]=""
    b16["text"]=""
    b17["text"]=""
    b18["text"]=""
    b19["text"]=""
    b20["text"]=""
    b21["text"]=""
    b22["text"]=""
    b23["text"]=""
    b24["text"]=""
    b25["text"]=""
    

    b1.configure(background="gainsboro")
    b2.configure(background="gainsboro")
    b3.configure(background="gainsboro")
    b4.configure(background="gainsboro")
    b5.configure(background="gainsboro")
    b6.configure(background="gainsboro")
    b7.configure(background="gainsboro")
    b8.configure(background="gainsboro")
    b9.configure(background="gainsboro")
    b10.configure(background="gainsboro")
    b11.configure(background="gainsboro")
    b12.configure(background="gainsboro")
    b13.configure(background="gainsboro")
    b14.configure(background="gainsboro")
    b15.configure(background="gainsboro")
    b16.configure(background="gainsboro")
    b17.configure(background="gainsboro")
    b18.configure(background="gainsboro")
    b19.configure(background="gainsboro")
    b20.configure(background="gainsboro")
    b21.configure(background="gainsboro")
    b22.configure(background="gainsboro")
    b23.configure(background="gainsboro")
    b24.configure(background="gainsboro")
    b25.configure(background="gainsboro")

def NewGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    
lblPlayerX = Label(RightFrame1,font=('arial',40,'bold'),text="Player X:",padx=2,pady=2,bg='Cadet Blue')
lblPlayerX.grid(row=0,column=0,sticky=W)

txtPlayerX = Label(RightFrame1,font=('arial',40,'bold'),bd=2,fg='black',textvariable=PlayerX,width=4,
                   justify=LEFT).grid(row=0,column=1)

lblPlayerO = Label(RightFrame1,font=('arial',40,'bold'),text="Player O:",padx=2,pady=2,bg='Cadet Blue')
lblPlayerO.grid(row=1,column=0,sticky=W)

txtPlayerO = Label(RightFrame1,font=('arial',40,'bold'),bd=2,fg='black',textvariable=PlayerO,width=4,
                   justify=LEFT).grid(row=1,column=1)

btnReset = Button(RightFrame2,text="Reset",font=('arial',40,'bold'),height=1,width=11,command=reset)
btnReset.grid(row=2,column=0,padx=6,pady=11)

btnNewgame= Button(RightFrame2,text="New Game",font=('arial',40,'bold'),height=1,width=11,command=reset)
btnNewgame.grid(row=3,column=0,padx=6,pady=10)


#create 25 btn
b1=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b1))
b1.grid(row=1, column=1)

b2=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b2))
b2.grid(row=1, column=2)

b3=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b3))
b3.grid(row=1, column=3)

b4=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b4))
b4.grid(row=1, column=4)

b5=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b5))
b5.grid(row=1, column=5)

b6=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b6))
b6.grid(row=2, column=1)

b7=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b7))
b7.grid(row=2, column=2)

b8=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b8))
b8.grid(row=2, column=3)

b9=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b9))
b9.grid(row=2, column=4)

b10=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b10))
b10.grid(row=2, column=5)

b11=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b11))
b11.grid(row=3, column=1)

b12=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b12))
b12.grid(row=3, column=2)

b13=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b13))
b13.grid(row=3, column=3)

b14=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b14))
b14.grid(row=3, column=4)

b15=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b15))
b15.grid(row=3, column=5)

b16=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b16))
b16.grid(row=4, column=1)

b17=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b17))
b17.grid(row=4, column=2)

b18=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b18))
b18.grid(row=4, column=3)

b19=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b19))
b19.grid(row=4, column=4)

b20=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b20))
b20.grid(row=4, column=5)

b21=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b21))
b21.grid(row=5, column=1)

b22=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b22))
b22.grid(row=5, column=2)

b23=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b23))
b23.grid(row=5, column=3)

b24=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b24))
b24.grid(row=5, column=4)

b25=Button(LeftFrame, text="", font=('Times 20 bold'),bg='white', height=3, width=6, command=lambda:btn_click(b25))
b25.grid(row=5, column=5)

#store btn in list
buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25]


if __name__=="__main__":
    root.mainloop()

        
