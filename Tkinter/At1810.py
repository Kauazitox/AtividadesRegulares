import tkinter as tk
class Tela:
    def __init__(self, master):
        self.nstela = master
        self.fr1 = tk.Frame (self.nstela)
        self.fr1.pack()
        self.fr2 = tk.Frame (self.nstela)
        self.fr2.pack()
        self.fr3 = tk.Frame (self.nstela)
        self.fr3.pack()

        self.bnt1 = tk.Button (self.fr1, text="1", width=3, height=2)
        self.bnt1.pack ()
        self.bnt2 = tk.Button (self.fr2, text="2", width=3, height=2)
        self.bnt2.pack (side=tk.LEFT)
        self.bnt3 = tk.Button (self.fr2, text="3", width=3, height=2)
        self.bnt3.pack (side=tk.LEFT)
        self.bnt4 = tk.Button (self.fr3, text="4", width=3, height=2)
        self.bnt4.pack (side=tk.LEFT)
        self.bnt5 = tk.Button (self.fr3, text="5", width=3, height=2)
        self.bnt5.pack (side=tk.LEFT)
        self.bnt6 = tk.Button (self.fr3, text="6", width=3, height=2)
        self.bnt6.pack (side=tk.LEFT)

janela = tk.Tk ()
Tela (janela)
janela.mainloop ()