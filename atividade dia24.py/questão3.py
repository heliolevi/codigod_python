def gerenciar_eventos():
    # Inicializa a lista de eventos
    eventos = []
    
    while True:
        print("\n--- Menu de Gerenciamento de Eventos ---")
        print("1. Adicionar evento")
        print("2. Remover evento")
        print("3. Exibir eventos")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            evento = input("Digite o nome do evento a ser adicionado: ")
            eventos.append(evento)
            print(f"Evento '{evento}' adicionado com sucesso!")
        
        elif escolha == "2":
            evento = input("Digite o nome do evento a ser removido: ")
            if evento in eventos:
                eventos.remove(evento)
                print(f"Evento '{evento}' removido com sucesso!")
            else:
                print(f"Evento '{evento}' não encontrado na lista.")
        
        elif escolha == "3":
            if eventos:
                print("\nEventos agendados para o mês:")
                for i, evento in enumerate(eventos, 1):
                    print(f"{i}. {evento}")
            else:
                print("Nenhum evento agendado.")
        
        elif escolha == "4":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


gerenciar_eventos()