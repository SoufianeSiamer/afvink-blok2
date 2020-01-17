from tkinter import *

tk = Tk()
tk.title("boter kaas en eggy")
bclick = True
flag = 0


def disablebutton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btnclick(buttons):
    global bclick, flag, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        flag += 1




buttons = StringVar()

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='black',
                 height=4, width=8, command=lambda: btnclick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
