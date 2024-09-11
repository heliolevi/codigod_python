#teste de condicional com números

valor = int(input("Informe um valor númerico: "))

if valor >= 50:
    print(f"O valor {valor} é maior ou igual a 50")
elif valor >=30 and valor < 50:
    print(f"o valor {valor} está entre 30 e 50\n")

else:
    print(f"o valor {valor} é menor que 50")

