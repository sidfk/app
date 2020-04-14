from tkinter import *
import tkinter.ttk as ttk
import sqlite3

t=Tk()
t.geometry('400x400')
t.title('Inventory')



menu = Menu(t) 
t.config(menu=menu) 

filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 

def add(e1,e2):
    name=e1.get()
    quantity=e2.get()


def additem():
    top=Toplevel()
    top.title('Add Item')
    top.geometry('400x200')
    l1=Label(top,text="Item Name :: ",font="ariel", padx=5, pady=5)
    l1.pack(pady=3)
    e1=Entry(top,font="ariel")
    e1.pack(pady=3)
    l2=Label(top,text="Quantity :: ",font="ariel", padx=5, pady=5)
    l2.pack(pady=3)
    e2=Entry(top,font="ariel")
    e2.pack(pady=3)
    b1=Button(top,text="Add",relief="raised", padx=5, pady=5)
    b1.pack(pady=3)


filemenu.add_command(label='Add Item', command=additem) 
filemenu.add_command(label='Add Item from File') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=t.quit) 

helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 

helpmenu.add_command(label='About') 


f1=Frame(t)
f1.pack()

btadd=Button(f1,text="Add item" , relief="raised", command=additem , padx=5, pady=5 )
btadd.pack(side=LEFT, padx=5, pady=5)
btaddfile=Button(f1,text="Add item from file" , relief="raised", padx=5, pady=5 )
btaddfile.pack(side=RIGHT, padx=5, pady=5)


f2=Frame(t)
f2.pack()

Scrollbar=Scrollbar(f2)
Scrollbar.pack(pady=10)

Scrollbar.pack( side = RIGHT, fill = Y ) 
mylist = Listbox(f2, yscrollcommand = Scrollbar.set ) 
for line in range(100): 
   mylist.insert(END, 'This is line number' + str(line)) 
mylist.pack( side = LEFT, fill = BOTH ) 
Scrollbar.config( command = mylist.yview )

t.mainloop()