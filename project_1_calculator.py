import tkinter.messagebox as tmsg
from tkinter import *

root = Tk()
root.geometry("250x300")
root.title("Arp's Calc")
# root.wm_iconbit.ico')
root.configure(background='black')

panel = StringVar();
panel.set("")
screen = Entry(root, textvar=panel, font='lucida 20 bold ', fg='light green', bg='black')
screen.pack(fill=X, padx=10, pady=10, ipadx=2, ipady=2)


def clickme(event):
    global panel
    content = event.widget.cget("text")
    # print(content)
    if content == '=':
        if panel.get().isdigit():
            value = int(panel.get())
        else:
            try:
                value = eval(panel.get())
                panel.set(value)
                screen.update()
            except Exception as e:

                tmsg.showinfo('Error', f'Sorry! "{panel.get()}" Not A Valid Expression\n'
                                       f'Press "C" To Clear...')
                panel.set('Press C')
                screen.update()


    elif content == 'C':
        panel.set("")
        screen.update()
    else:
        panel.set(str(panel.get()) + str(content))
        screen.update()


f = Frame(root, bg='black')
b = Button(f, text='C', padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text='%', padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text="/", padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text="*", padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
# b=Button(f,text=9,padx=10,pady=5,font='lucida 10 bold',bg='orange', fg='black').pack(side=LEFT)
f.pack()

f = Frame(root, bg='black')
b = Button(f, text=7, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text=8, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text=9, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text="+", padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
# b=Button(f,text=9,padx=10,pady=5,font='lucida 10 bold',bg='orange', fg='black').pack(side=LEFT)
f.pack()

f = Frame(root, bg='black')
b = Button(f, text=4, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text=5, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text=6, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text="-", padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
# b=Button(f,text=9,padx=10,pady=5,font='lucida 10 bold',bg='orange', fg='black').pack(side=LEFT)
f.pack()

f = Frame(root, bg='black')
b = Button(f, text=1, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text=2, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text=3, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text="^", padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
# b=Button(f,text=9,padx=10,pady=5,font='lucida 10 bold',bg='orange', fg='black').pack(side=LEFT)
f.pack()

f = Frame(root, bg='black')
b = Button(f, text=0, padx=10, pady=5, font='lucida 10 bold', bg='orange', fg='black')
b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text=".", padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text="=", padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
b = Button(f, text="**", padx=10, pady=5, font='lucida 10 bold', bg='blue', fg='yellow')

b.pack(side=LEFT, padx=2, pady=5)
b.bind("<Button-1>", clickme)
# b=Button(f,text=9,padx=10,pady=5,font='lucida 10 bold',bg='orange', fg='black').pack(side=LEFT)
f.pack()
root.mainloop()
