import random

def jogar():
    escolhas = ["Pedra", "Papel", "Tesoura"]
    
    # Escolha do computador e do usuário
    escolha_computador = random.randint(0, 2)
    escolha_usuario = int(input("Escolha 0 (Pedra), 1 (Papel) ou 2 (Tesoura): "))
    
    # Exibe as escolhas
    print(f"Você escolheu: {escolhas[escolha_usuario]}")
    print(f"Computador escolheu: {escolhas[escolha_computador]}")
    
    # Verifica o resultado
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (escolha_usuario == 0 and escolha_computador == 2) or \
         (escolha_usuario == 1 and escolha_computador == 0) or \
         (escolha_usuario == 2 and escolha_computador == 1):
        return "Você venceu!"
    else:
        return "Você perdeu!"

# Jogo
while True:
    print(jogar())
    if input("Jogar novamente? (s/n): ").lower() != 's':
        break