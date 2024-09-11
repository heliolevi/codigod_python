numero = int(input("Digite um número inteiro: "))


print(f"Divisores de {numero}: ")
for cons in range(1, numero +1):
    if numero % cons == 0:
         print(cons)