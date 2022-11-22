import tkinter as tk
class Tela:
    def __init__(self, master):
        self.nstela = master

        self.tx1 = tk.Label(self.nstela, text="Insira seu nome:")
        self.tx1.pack(side=tk.LEFT)

        self.entrada = tk.Entry(self.nstela)
        self.entrada.pack(side=tk.LEFT)
        self.btn = tk.Button(self.nstela, text="Confirmar", bg="green", command=self.mstnome)
        self.btn.pack(side=tk.LEFT, padx=10)

    def mstnome(self):
        self.nome = self.entrada.get()
        print("Ola, " + self.nome)

janela = tk.Tk()
Tela(janela)
janela.mainloop()