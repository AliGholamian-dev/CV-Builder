import tkinter as tk
import PyPDF2
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfile
from tkinter import BOTH, END, LEFT
from tkinter import ttk

root = tk.Tk()


canvas1 = tk.Canvas(root, width = 1300, height = 1000, relief = 'raised')
canvas1.pack()
bg = tk.PhotoImage(file = "Back02.png")

# Show image using label
canvas1.create_image(0,0, image = bg, anchor="nw")


#titles
canvas1.create_text(650, 50, text='Resume Creator', font=("Arial", 35), fill="white")
canvas1.create_text(650, 90, text='Create & Design by Ali Safarpour & Ali Gholamian', font=("Arial", 10), fill="white")
canvas1.create_text(300, 150, text='General Info', font=("Arial", 20), fill="white")
canvas1.create_text(960, 150, text='Skill Info', font=("Arial", 20), fill="white")


#box
entry1 = tk.Entry (root)
canvas1.create_window(470, 250, window=entry1, width=300)
canvas1.create_text(340, 228, text='Name', font=("Arial", 11), fill="white")

entry2 = tk.Entry (root)
canvas1.create_window(470, 308, window=entry2, width=300)
canvas1.create_text(355, 286, text='Last Name', font=("Arial", 11), fill="white")

entry3 = tk.Entry (root)
canvas1.create_window(470, 366, window=entry3, width=300)
canvas1.create_text(345, 344, text='Birthday', font=("Arial", 11), fill="white")

entry4 = tk.Entry (root)
canvas1.create_window(470, 424, window=entry4, width=300)
canvas1.create_text(370, 402, text='Phone Number', font=("Arial", 11), fill="white")

entry5 = tk.Entry (root)
canvas1.create_window(470, 482, window=entry5, width=300)
canvas1.create_text(348, 460, text='Address', font=("Arial", 11), fill="white")

entry6 = tk.Entry (root)
canvas1.create_window(470, 540, window=entry6, width=300)
canvas1.create_text(348, 518, text='Website', font=("Arial", 11), fill="white")

entry7 = tk.Text (root)
entry7.pack()
canvas1.create_window(470, 668, window=entry7, width=300, height=150)
canvas1.create_text(350, 581, text='About Me', font=("Arial", 11), fill="white")

#SKILL boxs Info

#skill box 1

entry12 = tk.Entry (root)
entry12.insert(0, "skill Name 1 :")
canvas1.create_window(900, 250, window=entry12, width=200)

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
canvas1.create_window(1075, 250, window=myCombo, width=100, height=22)


#skill box 2

entry13 = tk.Entry (root)
entry13.insert(0, "skill Name 2 :")
canvas1.create_window(900, 290, window=entry13, width=200)

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
canvas1.create_window(1075, 290, window=myCombo, width=100, height=22)


#skill box 3

entry14 = tk.Entry (root)
entry14.insert(0, "skill Name 3 :")
canvas1.create_window(900, 330, window=entry14, width=200)

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
canvas1.create_window(1075, 330, window=myCombo, width=100, height=22)


#skill box 4

entry13 = tk.Entry (root)
entry13.insert(0, "skill Name 4 :")
canvas1.create_window(900, 370, window=entry13, width=200)

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
canvas1.create_window(1075, 370, window=myCombo, width=100, height=22)




#skill box 5

entry13 = tk.Entry (root)
entry13.insert(0, "skill Name 5 :")
canvas1.create_window(900, 410, window=entry13, width=200)

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
canvas1.create_window(1075, 410, window=myCombo, width=100, height=22)


#MORE Info


#More info box
entry31 = tk.Text (root)
entry31.pack()
canvas1.create_window(965, 580, window=entry31, width=350, height=175)
canvas1.create_text(820, 478, text='Education', font=("Arial", 11), fill="white")

entry32 = tk.Text (root)
entry32.pack()
canvas1.create_window(965, 830, window=entry32, width=350, height=175)
canvas1.create_text(825, 728, text='Experience', font=("Arial", 11), fill="white")


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
browse_btnavatar = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="#00a9e2", fg="white", height=10, width=22)
browse_text.set("Your Avatar")
canvas1.create_window(170, 350, window=browse_btnavatar)



#Template
def open_file():
    browse_text.set("loading..")
    file = askopenfile(parent=root, mode='rb', title="choose a file", filetype=[("jpg file", "*.jpg")] )
    if file:
        print("ok")

    browse_text.set("Create")


browse_text = tk.StringVar()
browse_btnavatar = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Arial", bg="#00a9e2", fg="white", height=1, width=30)
browse_text.set("Create")
canvas1.create_window(650, 970, window=browse_btnavatar)



root.mainloop()
