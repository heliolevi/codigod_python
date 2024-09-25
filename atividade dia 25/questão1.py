def catalogo_livros():
    catalogo = {}
    while True:
        opcao = input("\n1. Adicionar livro\n2. Remover livro\n3. Exibir catálogo\n4. Sair\nEscolha: ")
        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            catalogo[titulo] = autor
        elif opcao == "2":
            titulo = input("Título a remover: ")
            catalogo.pop(titulo, None)
        elif opcao == "3":
            for titulo, autor in catalogo.items():
                print(f"{titulo} - {autor}")
            print(f"Total de livros: {len(catalogo)}")
        elif opcao == "4":
            break