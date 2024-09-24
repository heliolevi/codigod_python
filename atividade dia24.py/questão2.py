def notas_acima_da_media():
    # uma lista para armazenar as notas
    notas = []
    
    # Solicita as notas do aluno até que seja digitado zero
    while True:
        nota = float(input("Digite a nota do aluno (0 para terminar): "))
        if nota == 0:
            break
        notas.append(nota)
    
    #  quantas notas são acima da média (7)
    acima_media = sum(1 for nota in notas if nota > 7)
    
    #  quantidade de alunos acima de 7
    print(f"Quantidade de alunos com nota acima de 7: {acima_media}")


notas_acima_da_media()