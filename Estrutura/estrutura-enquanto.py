contador = 1 #while é obrigatorio inicializar a variável

while contador <=5: 
    print(contador)
    contador = contador + 1 #contador += 1

print("="*40)

    #2ª FORMA DE UTILIZAR while

x = 0

while x >= 0:
    x = int(input("Informe um valor qualquer(digite um valor negativo para terminar): "))
    print(F"Você digitou {x} ")

print("="*40)

#3ª forma de utilizar while - como se fosse faça...enquanto

while True:
    y = input("Informe a senha: ")
    if y == "123":
        print("Parabéns senha correta")
        break #forma de encerrar o while
    else:
        print("Senha errada, sai fora")