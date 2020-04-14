import tkinter as tk
root = tk.Tk()
root.title("List App")
root.geometry("1000x1000")
def clicked():
	listbox.insert(tk.END, content.get())

def delete():
	listbox.delete(0, tk.END)

def delete_selected():
	listbox.delete(tk.ANCHOR)


content = tk.StringVar()
l=tk.Label(root,text="Enter Item").place(x=0,y=0)
entry = tk.Entry(root, textvariable=content).place(x=60,y=0)
button = tk.Button(root, text="Add Item", command=clicked).place(x=130,y=0)
button_delete = tk.Button(text="Delete All", command=delete).place(x=190,y=0)
button_delete_selected = tk.Button(text="Delete Selected", command=delete_selected).place(x=252,y=0)

listbox = tk.Listbox(root)
listbox.place(x=5,y=20)
root.mainloop()

