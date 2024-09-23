lista = []
for i in range (10):
    valor = int(input(f"Digite o valor {i+1}: "))

    lista.append(valor)

for i in range (len(lista)):  #retorna o número de elementos de um objeto, como uma string, lista, tupla, dicionário ou qualquer sequência
    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            print(f"Elemento igual {lista[i]} encontrado nas posições {i} e {j}")  