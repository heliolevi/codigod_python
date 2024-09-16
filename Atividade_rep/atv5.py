import random

# Contadores para cada número de 1 a 6
contagem = {i: 0 for i in range(1, 7)}

# Lançar o dado 10 vezes
for _ in range(10):
    resultado = random.randint(1, 6)
    contagem[resultado] += 1

# Mostrar quantas vezes cada número apareceu
for numero, vezes in contagem.items():
    print(f"O número {numero} saiu {vezes} vezes")
