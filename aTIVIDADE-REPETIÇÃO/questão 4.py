numero1 = int(input("Digite um numero:" ))
numero2 = int(input("Digite um numero maior que o anterior:" ))
soma = 0


for cons in range(numero1, numero2 +1):
    soma += cons
    print(f"a soma dos numeros inteiros de {numero1} a {numero2} é: {soma}")