usuario =input("Usuario: ")

while True:
    senha = input("Senha: ")
    if senha == usuario:
        print("conta criada")
        break

while True: 
    usuario2 = input("Usuario: ")
    if usuario2 == usuario:
        print ("Este usuario já existe")
    senha2 = input("Senha: ")
    if senha2 == senha:
        print("Está senha ja existe")
        