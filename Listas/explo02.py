print("Entre com números positivos: ")
lista = []

while True:
    p = int(input())
    if p <= 0:
        break
    lista.append(p)
x = int(input("Qual valor devo procurar? "))
if x in lista:
    print(x, "pertence à lista!")
else:
    print(x, "Não pertence à lista!")
