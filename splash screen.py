from tkinter import*
from PIL import Image

splash=Tk()
height=500
width=900
x=(splash.winfo_screenwidth()//2)-(width//2)
y=(splash.winfo_screenheight()//2)-(height//2)
splash.geometry('{}x{}+{}+{}'.format(width,height,x,y))
splash.configure(bg="black")
    
backgroundImage=PhotoImage(file="E:\\Tic-tac-toe\\Tic-tac-toe\\background.png")
bg_image=Label(
    splash,
    image=backgroundImage
)
bg_image.pack()
 
splash.overrideredirect(True)

label1=Label(splash,text=" Tic Tac Toe", font=("yu gothic ui bold",35 *-1),bg="black",fg="#FFFFFF")
label1.place(x=380,y=110)

label1=Label(splash,text=" Loading game...", font=("yu gothic ui bold",20 *-1),bg="black",fg="#FFFFFF")
label1.place(x=390,y=180)

gifImage="E:\\Tic-tac-toe\\Tic-tac-toe\\img1.gif"

openImage=Image.open(gifImage)

frames=openImage.n_frames

imageObject=[PhotoImage(file=gifImage,format=f'gif -index {i}')for i in range(frames)]

count=1

showAnimation=None

def animation(count):
    global showAnimation
    newImage=imageObject[count]

    gif_Label.configure(image=newImage)
    count +=1
    if count == frames:
        count=0
    showAnimation=splash.after(50,lambda:animation(count))

gif_Label=Label(splash,image="")
gif_Label.place(x=150,y=240,width=600,height=100)

def main_window():
    splash.withdraw()
    import level

    window=Tk()
    window.configure(bg="black")
    
    height=650
    width=1240
    x=(window.winfo_screenwidth()//2)-(width//2)
    y=(window.winfo_screenheight()//2)-(height//2)
    window.geometry('{}x{}+{}+{}'.format(width,height,x,y))

    
#splash screen
splash.after(8000,main_window)
animation(count)
splash.mainloop()
