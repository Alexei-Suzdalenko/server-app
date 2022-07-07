import tkinter as tk

windowApp = tk.Tk()

class App:
    def __init__(self):
        pass

    def init_app(self):
        windowApp.title('Gráficos Froxa')
        windowApp.geometry('350x200')
        windowApp.resizable(False, False)
        windowApp.rowconfigure(4, minsize=50)
        windowApp.columnconfigure((0, 1, 2, 3, 4), minsize=50)

        text_label0 = tk.Label(text="")
        text_label0.grid(row=0, column=0)
        text_label = tk.Label(text="")
        text_label.grid(row=1, column=1)
        text_label1 = tk.Label(text="Froxa App")
        text_label1.grid(row=2, column=3)

        windowApp.mainloop()
