#Programa que joga impar par com o computador, O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou ao final do jogo
from random import randint
print(30*'-')
print('VAMOS JOGAR PAR OU IMPAR')
print(30*'-')
total = 0
while True: 
    player = int(input('Digite um número: '))
    escolha = input('Qual sua escolha? [ I / P ]\n').strip().upper()
    computador = randint(0, 10)
    if (player + computador) % 2  == 0:
        if escolha == 'P':
            print(f'Você jogou {player} e o computador jogou {computador}, total de {player + computador}, Deu PAR\nVOCÊ VENCEU!!!')
            print(30*'-')
            print('Vamos jogar novamente....')
            total += 1
        elif escolha == 'I':
            break
        else:
            print('ERRO!!! Digite uma valor valido: [ I / P ]')
            print(30*'-')
    else: 
        if escolha == 'I':
            print(f'Você jogou {player} e o computador jogou {computador}, total de {player + computador}, Deu IMPAR\nVOCÊ VENCEU!!!')
            print(30*'-')
            print('Vamos jogar novamente....')
            total += 1
        elif escolha == 'P':
            break
        else:
            print('ERRO!!!\nDigite uma valor valido: [ I / P ]')
            print(30*'-')
if escolha == 'P':
    print(f'Você jogou {player} e o computador jogou {computador}, total de {player + computador}, Deu IMPAR\nVOCÊ PERDEU!!!')
elif escolha == 'I':
    print(f'Você jogou {player} e o computador jogou {computador}, total de {player + computador}, Deu PAR\nVOCÊ PERDEU!!!')
print(f"IT'S OVER!!! Você venceu {total} vezes")

