def notas_alunos():
    alunos = {}
    while True:
        nome = input("Aluno (ou 'sair'): ")
        if nome == 'sair': break
        alunos[nome] = float(input("Nota: "))
    
    media = sum(alunos.values()) / len(alunos)
    print(f"Média da turma: {media:.2f}")
    print("Alunos acima da média:")
    for nome, nota in alunos.items():
        if nota > media:
            print(f"{nome}: {nota:.2f}")

