import tkinter as tk
import PyPDF2
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfile
from tkinter import BOTH, END, LEFT
from tkinter import ttk

root = tk.Tk()


canvas1 = tk.Canvas(root, width = 1600, height = 800, relief = 'raised')
canvas1.pack()

#title
label1 = tk.Label(root, text='Resume Creator')
label1.config(font=('Arial', 18))
canvas1.create_window(800, 25, window=label1)

#boxs Info
label2 = tk.Label(root, text='General Info')
label2.config(font=('Arial', 14))
canvas1.create_window(200, 60, window=label2)


#box
entry1 = tk.Entry (root)
entry1.insert(0, "Your Name :")
canvas1.create_window(200, 100, window=entry1, width=200)

entry2 = tk.Entry (root)
entry2.insert(0, "Your Last Name :")
canvas1.create_window(200, 140, window=entry2, width=200)

entry3 = tk.Entry (root)
entry3.insert(0, "birthday :")
canvas1.create_window(200, 180, window=entry3, width=200)

entry4 = tk.Entry (root)
entry4.insert(0, "Phone Number :")
canvas1.create_window(200, 220, window=entry4, width=200)

entry5 = tk.Entry (root)
entry5.insert(0, "Address :")
canvas1.create_window(200, 260, window=entry5, width=200)

entry6 = tk.Entry (root)
entry6.insert(0, "Website :")
canvas1.create_window(200, 300, window=entry6, width=200)

entry7 = tk.Text (root)
entry7.pack()
entry7.insert("end", "About me :")
canvas1.create_window(200, 410, window=entry7, width=200, height=150)

#SKILL boxs Info
label2 = tk.Label(root, text='Skills Info')
label2.config(font=('Arial', 14))
canvas1.create_window(600, 60, window=label2)

#skill box 1

entry12 = tk.Entry (root)
entry12.insert(0, "skill Name 1 :")
canvas1.create_window(600, 100, window=entry12, width=200)

def comboclick(event):
    if myCombo.get() == 'master':
        myLabel = tk.Label(root, text="wow")
        myLabel.pack()
    else:
        myLabel = tk.Label(root, text=myCombo.get()).pack()

options = [
    "beginner",
    "Mid Level",
    "master"
]

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
canvas1.create_window(775, 100, window=myCombo, width=100, height=22)


#skill box 2

entry13 = tk.Entry (root)
entry13.insert(0, "skill Name 2 :")
canvas1.create_window(600, 140, window=entry13, width=200)

def comboclick(event):
    if myCombo.get() == 'master':
        myLabel = tk.Label(root, text="wow")
        myLabel.pack()
    else:
        myLabel = tk.Label(root, text=myCombo.get()).pack()

options = [
    "beginner",
    "Mid Level",
    "master"
]

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
canvas1.create_window(775, 140, window=myCombo, width=100, height=22)


#skill box 3

entry14 = tk.Entry (root)
entry14.insert(0, "skill Name 3 :")
canvas1.create_window(600, 180, window=entry14, width=200)

def comboclick(event):
    if myCombo.get() == 'master':
        myLabel = tk.Label(root, text="wow")
        myLabel.pack()
    else:
        myLabel = tk.Label(root, text=myCombo.get()).pack()

options = [
    "beginner",
    "Mid Level",
    "master"
]
myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
canvas1.create_window(775, 180, window=myCombo, width=100, height=22)


#skill box 4

entry13 = tk.Entry (root)
entry13.insert(0, "skill Name 4 :")
canvas1.create_window(600, 220, window=entry13, width=200)

def comboclick(event):
    if myCombo.get() == 'master':
        myLabel = tk.Label(root, text="wow")
        myLabel.pack()
    else:
        myLabel = tk.Label(root, text=myCombo.get()).pack()

options = [
    "beginner",
    "Mid Level",
    "master"
]

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
canvas1.create_window(775, 220, window=myCombo, width=100, height=22)




#skill box 5

entry13 = tk.Entry (root)
entry13.insert(0, "skill Name 5 :")
canvas1.create_window(600, 260, window=entry13, width=200)

def comboclick(event):
    if myCombo.get() == 'master':
        myLabel = tk.Label(root, text="wow")
        myLabel.pack()
    else:
        myLabel = tk.Label(root, text=myCombo.get()).pack()

options = [
    "beginner",
    "Mid Level",
    "master"
]

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
canvas1.create_window(775, 260, window=myCombo, width=100, height=22)


#MORE Info
label2 = tk.Label(root, text='More Info')
label2.config(font=('Arial', 14))
canvas1.create_window(1250, 60, window=label2)

#More info box
entry31 = tk.Text (root)
entry31.pack()
entry31.insert("end", "Education :")
canvas1.create_window(1250, 175, window=entry31, width=500, height=175)

entry32 = tk.Text (root)
entry32.pack()
entry32.insert("end", "Experience :")
canvas1.create_window(1250, 425, window=entry32, width=500, height=175)


#function last botton
def open_file():
    button1.set("loading..")
    file = askopenfile(parent=root, mode='rb', title="choose a file", filetype=[("jpg file", "*.jpg")] )
    if file:
        print("ok")
    browse_text.set("Create Resume")

#create resume button
browse_text = tk.StringVar()
button1 = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="#00a9e2", fg="white", height=1, width=20 )
canvas1.create_window(1450, 750, window=button1)
browse_text.set("Create Resume")

#Avatar
def open_file():
    browse_text.set("loading..")
    file = askopenfile(parent=root, mode='rb', title="choose a file", filetype=[("jpg file", "*.jpg")] )
    if file:
        print("ok")

    browse_text.set("Your Avatar")

#Avatar button
browse_text = tk.StringVar()
browse_btnavatar = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="#00a9e2", fg="white", height=1, width=15)
browse_text.set("Your Avatar")
canvas1.create_window(200, 700, window=browse_btnavatar)



#Template
def open_file():
    browse_text.set("loading..")
    file = askopenfile(parent=root, mode='rb', title="choose a file", filetype=[("jpg file", "*.jpg")] )
    if file:
        print("ok")

    browse_text.set("Choose Your Template")


browse_text = tk.StringVar()
browse_btnavatar = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="#00a9e2", fg="white", height=1, width=20)
browse_text.set("Choose Your Template")
canvas1.create_window(650, 700, window=browse_btnavatar)



root.mainloop()
