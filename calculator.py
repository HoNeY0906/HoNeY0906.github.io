from  tkinter import*

def click(event):
    global svalue
    text =event.widget.cget("text")
    print(text)
    if text =="=":
        if svalue.get().isdigit():
            Value = int(svalue.get())
        else:
             Value = eval(svalue.get())
        svalue.set(Value)
        screen.update

    elif text =="C":
        svalue.set("")
        screen.update()
    else:
        svalue.set(svalue.get() + text)
        screen.update()

root = Tk()

root.geometry("544x600")
root.title("Calculator By Aman Umre")
root.wm_iconbitmap("")


svalue = StringVar()
svalue.set("")
screen=Entry(root, textvar=svalue, font="license 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)


f1= Frame(root,bg="grey")

b=Button(f1,text="C",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="%",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="X",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="/",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

f1.pack()

f1= Frame(root,bg="grey")

b=Button(f1,text="7",padx=18,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="8",padx=18,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="9",padx=18,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="*",padx=18,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

f1.pack()



f1= Frame(root,bg="grey")

b=Button(f1,text="4",padx=18,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="5",padx=18,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="6",padx=18,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="-",padx=19,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

f1.pack()

f1= Frame(root,bg="grey")

b=Button(f1,text="1",padx=16,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="2",padx=17,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="3",padx=17,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="+",padx=17,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

f1.pack()

f1= Frame(root,bg="grey")

b=Button(f1,text="00",padx=6,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="0",padx=19,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text=".",padx=19,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b=Button(f1,text="=",padx=17,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

f1.pack()

root.mainloop()

