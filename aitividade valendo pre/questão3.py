def calcular_bonus(salario, anos_servico):
    if anos_servico <= 5:
        bonus = salario * 0.05
    elif anos_servico <= 10:
        bonus = salario * 0.10
    else:
        bonus = salario * 0.15
    return bonus


salario = float(input("Qual é o seu salário atual? "))
anos_servico = int(input("Quantos anos de serviço você tem? "))


bonus = calcular_bonus(salario, anos_servico)
salario_final = salario + bonus


print(f"Bônus: R$ {bonus:.2f}")
print(f"Salário final com bônus: R$ {salario_final:.2f}")