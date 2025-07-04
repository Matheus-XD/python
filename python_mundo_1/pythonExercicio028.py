#Programa que faz o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual numero pensado
#pelo computador e dizer se estava correto ou errado


import random

lista = [0, 1, 2, 3, 4, 5]
numero = random.choice(lista)

escolher = int(input('Digite um número entre 0 e 5: '))

if escolher == numero:
    print('você está correto, o numero escolhido pelo computador é {} e o numero escolhido por você é {}'.format(numero, escolher))
else:
    print('Voce está errado, o numero escolhido pelo computador é {} e o numero escolhido por vc é {}'.format(numero, escolher))