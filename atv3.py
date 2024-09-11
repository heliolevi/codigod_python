temperaturas = [float(input("Digite a temperatura: ")) for _ in range(7)]

acima_ou_igual = 0
abaixo = 0

for temp in temperaturas:
    if temp >= 33.5:
        acima_ou_igual += 1
    else:
        abaixo += 1

print(f"Temperaturas iguais ou acima de 33.5: {acima_ou_igual}")
print(f"Temperaturas abaixo de 33.5: {abaixo}")
