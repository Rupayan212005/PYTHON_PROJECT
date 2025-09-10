from tkinter import *


root=Tk()
myentry1=Entry(root,width=35,borderwidth=5,bg="#808080")
myentry1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
myentry1.focus_set()
root.title("caccu")





def buttonclick(number):
    cclick=myentry1.get()
    myentry1.delete(0,END)
    myentry1.insert(0,str(cclick) + str(number))


def clear():
    myentry1.delete(0,END)

def add():
    firstnum=myentry1.get()
    global fnumber
    global math
    math="addition"
    fnumber=int(firstnum)
    myentry1.delete(0,END)

def sub():
    firstnum=myentry1.get()
    global fnumber
    global math
    math="subtraction"
    fnumber=int(firstnum)
    myentry1.delete(0,END)

def mul():
    firstnum=myentry1.get()
    global fnumber
    global math
    math="multiplication"
    fnumber=int(firstnum)
    myentry1.delete(0,END)

def div():
    firstnum=myentry1.get()
    global fnumber
    global math
    math="divistion"
    fnumber=int(firstnum)
    myentry1.delete(0,END)


def equal():
    secnum=myentry1.get()
    myentry1.delete(0,END)

    if math=="addition":
        myentry1.insert(0,int(fnumber)+int(secnum))
    elif math=="subtraction":
        myentry1.insert(0,int(fnumber)-int(secnum))  
    elif math=="multiplication":
        myentry1.insert(0,int(fnumber)*int(secnum))
    elif math=="divistion":
        myentry1.insert(0,int(fnumber)/int(secnum))





mybutton1=Button(root,text="1",padx=40,pady=20,bg="#FFC0CB",command=lambda:buttonclick(1))
mybutton2=Button(root,text="2",padx=40,pady=20,bg="#FFC0CB",command=lambda:buttonclick(2))
mybutton3=Button(root,text="3",padx=40,pady=20,bg="#FFC0CB",command=lambda:buttonclick(3))
mybutton4=Button(root,text="4",padx=40,pady=20,bg="#FFFFC5",command=lambda:buttonclick(4))
mybutton5=Button(root,text="5",padx=40,pady=20,bg="#FFFFC5",command=lambda:buttonclick(5))
mybutton6=Button(root,text="6",padx=40,pady=20,bg="#FFFFC5",command=lambda:buttonclick(6))
mybutton7=Button(root,text="7",padx=40,pady=20,bg="#CBC3E3",command=lambda:buttonclick(7))
mybutton8=Button(root,text="8",padx=40,pady=20,bg="#CBC3E3",command=lambda:buttonclick(8))
mybutton9=Button(root,text="9",padx=40,pady=20,bg="#CBC3E3",command=lambda:buttonclick(9))
mybutton0=Button(root,text="0",padx=40,pady=20,bg="#CBC3E3",command=lambda:buttonclick(0))



mybuttonadd=Button(root,text="+",padx=40,pady=20,bg="#FF0000",command=add)
mybuttonminus=Button(root,text="-",padx=40,pady=20,bg="#FF0000",command=sub)
mybuttondiv=Button(root,text="%",padx=40,pady=20,bg="#FF0000",command=div)
mybuttonmul=Button(root,text="x",padx=40,pady=20,bg="#FF0000",command=mul)
mybuttonequal=Button(root,text="=",padx=40,pady=20,bg="#239b56",command=equal)
mybuttonclear=Button(root,text="c",padx=40,pady=20,bg="#239b56",command=clear)


mybutton1.grid(row=3,column=0)
mybutton2.grid(row=3,column=1)
mybutton3.grid(row=3,column=2)
mybutton4.grid(row=4,column=0)
mybutton5.grid(row=4,column=1)
mybutton6.grid(row=4,column=2)
mybutton7.grid(row=5,column=0)
mybutton8.grid(row=5,column=1)
mybutton9.grid(row=5,column=2)
mybutton0.grid(row=6,column=0)


mybuttonadd.grid(row=6,column=1)
mybuttonminus.grid(row=6,column=2)
mybuttondiv.grid(row=7,column=0)
mybuttonmul.grid(row=7,column=1)
mybuttonequal.grid(row=7,column=2)
mybuttonclear.grid(row=8,column=1)






root.mainloop()