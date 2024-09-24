def intersecao_listas():
    
    lista1 = list(map(int, input("Digite os números da primeira lista separados por espaço: ").split()))
    lista2 = list(map(int, input("Digite os números da segunda lista separados por espaço: ").split()))
    
    # Encontra a interseção e exibe em ordem crescente
    intersecao = sorted(set(lista1) & set(lista2))
    
    print(f"Interseção entre as listas: {intersecao}")

    intersecao_listas()