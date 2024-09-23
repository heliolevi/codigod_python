import time

def cronometro(tempo):
    for i in range(1, tempo + 1):
        print(f"{i}...")
        time.sleep(1)  # Pausa de 1 segundo

# Entrada do usuário
tempo = int(input("Digite o tempo em segundos: "))