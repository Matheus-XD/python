#Programa que faz o computador jogar jokenpô com o usuario

import random

player = input('Digite qual a sua jogada: Pedra, Papel ou Tesoura: ').lower().strip()


comandos = ['pedra', 'papel', 'tesoura']
maquina = random.choice(comandos).lower().strip()

print('A maquina escolheu: {}\nVocê escolheu {}' .format(maquina, player))

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

