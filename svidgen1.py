from tkinter import *
from tkinter import messagebox 
root = Tk()
root.title("sss")
root.geometry("720x1280")

"""main_menu = Menu()
file_menu = Menu(font=("Verdana", 10, "bold"), tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")"""

"""l1 = Label(bg="lightgreen", width = 10, height = 2, text = "")
l1.pack(expand=1, anchor=S)
l1.pack()

def check():
	answer = mb.askyesno(title="window", message="hell0")
message = StringVar()

b = Button(text='fff',width  = 100, height = 2, command=check).place(x=800, y=676)

e1 = Entry(root, text='', width = 90, textvariable=message).place(y=686)"""


def display_full_name():
		messagebox.showinfo("Python", name.get() + " " + surname.get())

name = StringVar()
surname = StringVar()
name_label = Label(text="Введите время:").place(x=800, y=600)
name_label.grid(row=0, column=0, sticky="w")
surname_label = Label(text="Введите бюджет:")
name_entry = Entry(textvariable=name)
surname_label.grid(row=1, column=0, sticky="w")
surname_entry = Entry(textvariable=surname)
name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)
message_button = Button(text="Click Me", command=display_full_name)
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")


root.mainloop()