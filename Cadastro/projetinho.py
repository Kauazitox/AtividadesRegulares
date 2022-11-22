from tkinter import *

#Codigo da pagina principal!
class Principal:
    def __init__(self, master):
        # Aqui criamos a janela e renderizamos sua logo!
        self.master = master
        self.master.title("Principal")
        self.img = PhotoImage(file="assets/logo03.png")
        self.photo = PhotoImage(file="assets/logo05.png")

        #Nesta parte é feita a criação dos comandos presentes na tela principal!
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.menu.add_command(label="Arquivo")
        self.menu.add_command(label="Cadastro", command=self.openCadastro)
        self.menu.add_command(label="Help", command=self.openHelp)

        #Aqui renderizamos a foto principal (A mais grande), juntamente com o icone da imagem!
        self.label = Label(self.master, image=self.img)
        self.label.pack()
        master.iconphoto(False, self.photo)

#Aqui faz com que a pagina Help seja aberta!
    def openHelp(self):
        self.newWindow = Toplevel()
        Help(self.newWindow)

#Aqui faz o mesmo processo mas neste caso abre a pagina Cadastro!
    def openCadastro(self):
        self.newWindow = Toplevel()
        Cadastrar(self.newWindow)

#Codigo da pagina Cadastro!
class Cadastrar:
    def __init__(self, screen):
        #Aqui criamos a janela e renderizamos sua logo!
        self.screen1 = screen
        self.screen1.title("Cadastro Funcionário")
        self.cds = PhotoImage(file="assets/logocds.png")

        #Aqui damos o nome da tabela!
        self.inputFrame = LabelFrame(self.screen1, text="Dados", bg="lightgray")
        self.inputFrame.grid(row=0, column=0, columnspan=2)

        #Aqui é aonde os textos são renderizados para aparecer em sua tela!
        self.cod = Label(self.inputFrame, text="Código:", font=("Arial 15"), bg="lightgray")
        self.cod.grid(row=0, column=0, pady=5, padx=5)
        self.name = Label(self.inputFrame, text="Nome:", font=("Arial 15"), bg="lightgray")
        self.name.grid(row=1, column=0, pady=5, padx=5)
        self.cpf = Label(self.inputFrame, text="CPF:", font=("Arial 15"), bg="lightgray")
        self.cpf.grid(row=2, column=0, pady=5, padx=5)
        self.fone = Label(self.inputFrame, text="Fone:", font=("Arial 15"), bg="lightgray")
        self.fone.grid(row=3, column=0, pady=5, padx=5)
        self.end = Label(self.inputFrame, text="Endereço:", font=("Arial 15"), bg="lightgray")
        self.end.grid(row=4, column=0, pady=5, padx=5)
        self.cidade = Label(self.inputFrame, text="Cidade:", font=("Arial 15"), bg="lightgray")
        self.cidade.grid(row=5, column=0, pady=5, padx=5)

        #Nesta parte do codigo é feito para que o usuario entre com os seus dados!
        self.codEntry = Label(self.inputFrame, relief="ridge", height=1, width=20)
        self.codEntry.grid(row=0, column=1, pady=5, padx=5)
        self.nameEntry = Entry(self.inputFrame)
        self.nameEntry.grid(row=1, column=1, pady=5, padx=5)
        self.cpfEntry = Entry(self.inputFrame)
        self.cpfEntry.grid(row=2, column=1, pady=5, padx=5)
        self.foneEntry = Entry(self.inputFrame)
        self.foneEntry.grid(row=3, column=1, pady=5, padx=5)
        self.endEntry = Entry(self.inputFrame)
        self.endEntry.grid(row=4, column=1, pady=5, padx=5)
        self.cidadeEntry = Entry(self.inputFrame)
        self.cidadeEntry.grid(row=5, column=1, pady=5, padx=5)

        self.frameButton = LabelFrame(self.screen1, text="", bg="lightgray")
        self.frameButton.grid(row=1, column=0, columnspan=2)

        #Nesta parte fizemos os botoes da pagina!
        self.saveButton = Button(self.frameButton, text="Salvar")
        self.saveButton.grid(row=5, column=0, pady=10)
        self.deleteButton = Button(self.frameButton, text="Deletar")
        self.deleteButton.grid(row=5, column=1, pady=10)
        self.exitButton = Button(self.frameButton, text="Sair", command=self.screen1.destroy)
        self.exitButton.grid(row=5, column=2, pady=10)

        screen.iconphoto(False, self.cds)

#Codigo da pagina Help!
class Help:
    def __init__(self, screen):
        # Aqui criamos a janela e renderizamos sua logo!
        self.screen = screen
        self.screen.title("Help")
        self.help = PhotoImage(file="assets/logohelp.png")

        #Nesta parte renderizamos os textos presentes na pagina help!
        self.text = Label(self.screen, text="Caso encontre problemas!")
        self.text.pack()

        self.text01 = Label(self.screen, text="gmail: kauaribeiro.capanema@gmail.com")
        self.text01.pack()

        self.text02 = Label(self.screen, text="Tele: (46) XXXXXXXX")
        self.text02.pack()

        #Nesta parte é feito o comando de fechar a pagina!
        self.button = Button(self.screen, text="Sair", command=self.screen.destroy)
        self.button.pack(side=RIGHT)

        screen.iconphoto(False, self.help)

#Aqui é o codigo aonde o programa é fechado!
    def exit(self):
        self.screen.quit()

