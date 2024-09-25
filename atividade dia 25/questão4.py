def calcular_desconto(valor, desconto):
    return valor - (valor * desconto / 100)

valores_com_desconto = []
for _ in range(5):
    valor = float(input("Valor: R$ "))
    desconto = float(input("Desconto (%): "))
    valores_com_desconto.append(calcular_desconto(valor, desconto))

print("Valores finais com desconto:", valores_com_desconto)