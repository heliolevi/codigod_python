def e_numero_perfeito(n):
    soma = sum(i for i in range(1, n) if n % i == 0)
    return soma == n

n = int(input("Digite um número inteiro: "))

if e_numero_perfeito(n):
    print(f"{n} é um número perfeito.")
else:
    print(f"{n} não é um número perfeito.")
