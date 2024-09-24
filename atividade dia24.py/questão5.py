import random

def lancar_moeda():
    # Lista contendo os dois valores: Cara e Coroa
    resultados_possiveis = ["Cara", "Coroa"]
    
    # Lista para armazenar os resultados dos lançamentos
    resultados = []
    
    while True:
        # Sorteia entre Cara e Coroa
        resultado = random.choice(resultados_possiveis)
        resultados.append(resultado)
        
        
        print(f"Resultado do lançamento: {resultado}")
        
        
        continuar = input("Deseja lançar a moeda novamente? (s/n): ").lower()
        if continuar != 's':
            break
    
    
    print(f"Lista de resultados: {resultados}")

# simulação de lançamento de moeda
lancar_moeda()