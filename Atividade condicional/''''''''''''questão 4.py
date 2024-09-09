altura = float(input("Qual sua altura em mestros"))
genero =(input("Digite o gênero (Homen/mulher): "))


if (genero == "homem"):
    peso_ideal = (72.7 * altura) - 58

elif (genero =="mulher"):
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = "Gênero inválido"

print(f"o peso ideal é: {peso_ideal:.2f} kg" if isinstance(peso_ideal, ))