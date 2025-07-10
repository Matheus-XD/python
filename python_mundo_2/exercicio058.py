#Programa que melhora o jogo do exercicio 028 onde o computador vai pensar um numero entre 0 e 10 só que agora o jogador vai tentar adivinhar até acertar e mostrando no final quantos palpites foram necessarios para vencer

#exercicio 028
#Programa que faz o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual numero pensado
#pelo computador e dizer se estava correto ou errado


import random

print('\033[33m##### JOGO DE ADIVINHAÇÕES #####\033[m')
escolha = int(input('Digite um número entre 0 e 10: '))
print('--------------------------------')
numero = random.randint(0,10)
palpites = 1

if escolha != numero:
    while escolha != numero:

        print('\033[31mVocê errou!!!\033[m')
        if escolha > numero:
            print('É um pouco menos')
        elif escolha < numero: 
            print('É um pouco mais')

        escolha = int(input('Tente novamente: '))
        print('--------------------------------')
        palpites += 1

print('\033[32mVOCÊ ACERTOU!!!\033[m\nO numero escolhido pelo computador é {}, você acertou em {} palpites'.format(numero, palpites))
print('--------------------------------')

    