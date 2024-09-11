''' Essa estrutura de repetição é o mais comum em qualquer outra
linguagem de progamação
for (contador = 1; contador <=5; contador++){

}

'''
#Exemplo 1º
for contador in range (1,6):
    print(contador)

print("-"*30)
#Exemplo 2º
for contador in range (1,11,2): #o 3º parâmetro irá aumentar o incremento dos valores que estão sendo exibidos
    print(contador)

print("-"*30)
#3º Exemplo - Números do maior para o menor
for contador in range (10,0,-1):
    print(contador,end=" ") # o comando end, informa como o python irá mostrar o final de uma exibição, por padrão irá dar um enter (/n)
