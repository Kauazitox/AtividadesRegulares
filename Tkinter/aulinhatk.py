#Aprendendo sobre a biblioteca TKINTER
from tkinter import *

janela = Tk()
janela.title("OLA MUNDO")
janela.geometry("600x250")

janela.config(bg="#0000CD")
janela.iconphoto(False, PhotoImage(file="logo.png"))

label_nome = Label(janela, width=14, height=2, text="Nome do Produto", font=("Arial 10 bold"), fg="black")
label_nome.grid(row=0, column=0, pady=10)

label_nome = Entry(janela, width=14)
label_nome.grid(row=0, column=4, pady=15)


label_idade = Label(janela, width=10, height=2, text="Valor:", font=("Arial 12 bold"), fg='black', bg="white")
label_idade.grid(row=1, column=0, pady=10)

label_idade = Entry(janela, width=14)
label_idade.grid(row=1, column=4, pady=15)


label_pais = Label(janela, width=10, height=2, text="Peso:", font=("Arial 12 bold"), fg="black", bg="white")
label_pais.grid(row=2, column=0, pady=10)

label_pais = Entry(janela, width=14)
label_pais.grid(row=2, column=4, pady=15)

label_peso = Label(janela, width=10, height=2, text="Peso:", font=("Arial 12 bold"), fg="black", bg="white")
label_peso.grid(row=3, column=0, pady=10)

label_peso = Entry(janela, width=14)
label_peso.grid(row=3, column=4, pady=15)

label_validade = Label(janela, width=10, height=2, text="Validade:", font=("Arial 12 bold"), fg="black", bg="white")
label_validade.grid(row=4, column=0, pady=10)

label_validade = Entry(janela, width=14)
label_validade.grid(row=4, column=4, pady=15)

label_origem = Label(janela, width=10, height=2, text="Origem:", font=("Arial 12 bold"), fg="black", bg="white")
label_origem.grid(row=5, column=0, pady=10)

label_origem = Entry(janela, width=14)
label_origem.grid(row=5, column=4, pady=15)


janela.mainloop()
