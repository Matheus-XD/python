'''frase = '     Matheus gostosão e comedor de pepecas rosinhas e suculentas    '

print(frase[13:21]) #mostra os caracteres que estão da posição 13 ate a 20 da string
print(frase[:21]) #mostra todos os caracteres de 0 ate o 20
print(frase[22:]) #mostra todos os caracteres de 22 ate o final da string
print(frase[:12:2]) #mostra todos os caracteres de 0 até 11 pulando de 2 em 2
print(frase.count('o')) #Mostra a quantidade de 'o' que tem na frase
print(len(frase.strip())) #Mostra o numero de caracters da frase sem contar os espaçoes na frente e atrás
print(len(frase)) #Mostra a quantidade total de caracteres da frase
print(frase.split()) #Divide a frase em uma lista sendo cada palavra um item da lista

lista = frase.split()
print(lista [5] [0:]) #printa o quinto item da lista e os caracteres de zero ate o final desse item'''

#-----------------------------------------------------------------------------------------------------------------

#programa que lê o nome de uma pessoa e mostre o nome com todas as letras maiúsculas, com todas as letras minusculas
#quantas letras ao todo (sem considerar os espaços) e quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ')

print('Nome: {}' .format(nome))
print('Nome em maiúsculo: {}' .format(nome.upper()))
print('Nome em minúsculo: {}' .format(nome.lower()))
print('quantidade de letras do nome: {}' .format(len(nome.strip()) - nome.count(' ')))
lista = nome.split()
print('quantidade de letras do primeiro nome: {} e tem {} letras' .format(lista [0] [0:], len(lista [0] [:])))