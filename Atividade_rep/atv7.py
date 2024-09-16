a = int(input("Digite o primeiro número inteiro positivo (a): "))
b = int(input("Digite o segundo número inteiro positivo (b): "))

contagem = 0

for i in range(a, b + 1):
    if i % 7 == 0 and i % 11 == 0:
        contagem += 1

print(f"Total de números entre {a} e {b} que são múltiplos de 7 e 11: {contagem}")
