n = int(input("Quantos números serão lidos? "))
lista = []
for i in range(n):
    print("Digite o", i,"valor: ")
    lista.append(int(input()))
x = int(input("Qual o número a procurar? "))
if x in lista:
    print(x, "pertence à lista")
else:
    print(x, "não pertence à lista")
