contador = 0
for cons in range (5):
    idade =int(input("Digite a idade: "))    

    if idade >= 18:
        contador += 1
    print(f"Quantidade de pessoas com 18 anos ou mais: {contador}")