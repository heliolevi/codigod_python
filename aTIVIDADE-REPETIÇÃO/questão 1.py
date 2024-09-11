soma =0 
contador = 0

for i in range(50, 71):
    if i % 2==0:
        soma += i
        contador += 1

media = soma / contador 

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Total de múmeros lidos: {contador}")