def cacular_multa(velocidade, limite):
    excesso = velocidade - limite
    if excesso <= 0:
        return "Sem multa"
    elif excesso <= 10:
        return "multa: R$ 50"
    elif excesso <= 20:
        return "multa: R$ 100"
    else:
        return "Multa: 200 R$"
    
velocidade = float(input("Qual foi a sua velocidade ?"))
limite = float(input("Qual seu limite ?"))

print(cacular_multa(velocidade, limite))
