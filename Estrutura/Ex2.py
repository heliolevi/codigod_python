nome = input ("Informe seu nome: ")
end= input("qual seu celular?")
igreja= input("Vamos na igreja ?")

#Exibindo dados das variáveis  
#print(nome, end, igreja)

#1 forma de concatenação
print("\nOlá, seu é", nome, "que nome bonito, seu celular é:", end, "e sua respota foi", igreja)

#2ª forma de concatenação

print("Olá {} seu numero é {} e sua idade é {}". format(nome, end, igreja))

#3ª forma de concatenação
print(f"Bem vind@ {nome}, você mora na {end} e sua resposta foi {igreja}")