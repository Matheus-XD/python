#Programa que lê 4 nomes e os ordena de forma aleatoria

import random

nomeUm = input('Digite o primeiro nome: ')
nomeDois = input('Digite o segundo nome: ')
nomeTres = input('Digite o terceiro nome: ')
nomeQuatro = input('Digite o quarto nome: ')

listaNomes = [nomeUm, nomeDois, nomeTres, nomeQuatro]

random.shuffle(listaNomes) #shuffle é uma função da biblioteca radom usada para embraralhar em ordem aleatoria os itens da lista

print('a ordem sorteada é {}' .format(listaNomes))