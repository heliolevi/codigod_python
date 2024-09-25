def comparar_idades(idade1, idade2):
    if idade1 > idade2: return "Primeira pessoa é mais velha."
    elif idade2 > idade1: return "Segunda pessoa é mais velha."
    return "Ambas têm a mesma idade."

while True:
    idade1 = int(input("Idade 1 (0 para sair): "))
    if idade1 == 0: break
    idade2 = int(input("Idade 2: "))
    print(comparar_idades(idade1, idade2))