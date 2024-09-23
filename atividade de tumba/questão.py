lista = []

for com in range (7):
    valor = int((input("dIGITE UM VALOR:")))

    lista.append(valor)

impares = 0
for num in lista:
    if num % 2 != 0:
        impares += 1

print("Quantidade de numeros impares:", impares)