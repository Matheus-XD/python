#Programa que faz o computador jogar jokenpô com o usuario

import random
import time


print(10*'=', 'JOKENPÔ', 10*'=')
player = input('Digite qual a sua jogada:\nPedra, Papel ou Tesoura? ').lower().strip()

comandos = ['pedra', 'papel', 'tesoura']
maquina = random.choice(comandos).lower().strip()
print(40*'=')

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ...')

print(40*'=')
print('A maquina escolheu: {}\nVocê escolheu {}' .format(maquina, player))
print(40*'=')
if player == maquina:
    print('O JOGO EMPATOU!!!')
elif player == 'pedra' and maquina == 'papel':
    print('A MAQUINA GANHOU!!!')
elif player == 'pedra' and maquina == 'tesoura':
    print('PARABÉNS VOCÊ GANHOU!!!')
elif player == 'papel' and maquina == 'pedra':
    print('PARABÉNS VOCÊ GANHOU!!!')
elif player == 'papel' and maquina == 'tesoura':
    print('A MAQUINA GANHOU!!!')
elif player == 'tesoura' and maquina == 'papel':
    print('PARABÉNS VOCÊ GANHOU!!!')
elif player == 'tesoura' and maquina == 'pedra':
    print('A MAQUINA GANHOU!!!')
else: 
    print('Algo de errado não está certo')

