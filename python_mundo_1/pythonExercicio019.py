#programa que lê 4 nomes e sorteia um deles

import random

nomeUm = str(input( 'Digite o primeiro nome: '))
nomeDois = (input('Digite o segundo nome: '))
nomeTres = input('Digite o terceiro nome: ')
nomeQuatro = input('Digite o quarto nome: ')

listaNomes = [nomeUm, nomeDois, nomeTres, nomeQuatro]
sorteado = random.choice(listaNomes)

print('O nome sorteado foi {}' .format(sorteado))