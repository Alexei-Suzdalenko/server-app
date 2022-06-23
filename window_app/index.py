import tkinter as tk


def start_window_app(root):
    root.rowconfigure(4, minsize=50)
    root.columnconfigure([0, 1, 2, 3], minsize=50)
   
    

    textLabel0 = tk.Label(text="") 
    textLabel0.grid(row=0, column=0) 
    textLabel = tk.Label( text="Hello, World!") 
    textLabel.grid(row=1, column=1) 
    textLabel1 = tk.Label( text="Hello, World!") 
    textLabel1.grid(row=2, column=2) 
    
    # textLabel.pack()
    root.title('Gráficos Froxa')
    root.geometry('350x200')
   
    root.mainloop()