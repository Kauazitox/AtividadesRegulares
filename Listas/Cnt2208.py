lista = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(lista[1:4])
print(lista[:3])
print(lista[-4:])
print(lista[::2])
print(lista[1::2])
print(lista[::-1])
lista[2]="GOOGLE"
print(lista)
lista[2:4] = ("BOB", "ROR")
print(lista)
lista[2:4] = [8, 8, 8]
print(lista)
lista[4:6] = []
print(lista)
print("BOB" in lista)
print(8 in lista)
lista.insert(2, "TENTATIVA")
lista.append("CONSEGUI")
lista.insert(len(lista), "FOFUFC")
print(lista)