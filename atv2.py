numeros = [float(input("Digite um número: ")) for _ in range(8)]

negativos = 0
soma_positivos = 0

for numero in numeros:
    if numero < 0:
        negativos += 1
    elif numero > 0:
        soma_positivos += numero

print(f"Quantidade de números negativos: {negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
