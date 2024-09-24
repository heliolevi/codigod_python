import random

def jogo_palavras():
    # Lista de palavras (usei a lista de animais, mas você pode escolher qualquer outra)
    palavras = ['leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 'hipopotamo', 
                'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 'pinguim', 'lobo']
    
    # Embaralha a lista de palavras
    lista_embaralhada = random.sample(palavras, len(palavras))
    
    # Escolhe uma palavra aleatória da lista
    palavra_aleatoria = random.choice(lista_embaralhada)
    
    # Informa ao usuário sobre as posições da lista
    print("A lista contém 15 itens, as posições vão de 0 a 14.")
    
    # Pergunta ao usuário em qual posição a palavra aleatória está na lista
    tentativas = 3
    acertou = False
    
    while tentativas > 0:
        try:
            posicao = int(input(f"Em qual posição está a palavra '{palavra_aleatoria}'? (0-14): "))
            if lista_embaralhada.index(palavra_aleatoria) == posicao:
                print("Parabéns, você acertou!")
                acertou = True
                break
            else:
                tentativas -= 1
                print(f"Você errou. Restam {tentativas} tentativas.")
        except ValueError:
            print("Por favor, insira um número válido entre 0 e 14.")
    
    if not acertou:
        posicao_correta = lista_embaralhada.index(palavra_aleatoria)
        print(f"Você não acertou. A palavra '{palavra_aleatoria}' estava na posição {posicao_correta}.")
    
    
    print(f"Lista embaralhada: {lista_embaralhada}")


jogo_palavras()