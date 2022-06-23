from tkinter import *

def clicked(textLabel):
        textLabel.configure(text = "I just got clicked")

def start_window_app(root):
    # place a label on the root window
    textLabel = root.Label(root, text="Hello, World!") 
    textLabel.grid() 
    
    btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
    # textLabel.pack()
    root.title('Server App')
    root.geometry('350x200')
    root.mainloop()