#Programa que ajuda um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 60 para cada jogo, cadastrando cada um em uma lista composta.
import random, time


numeroJogos = int(input('Número de jogos: '))

lista = []
jogo = []

for i in range(0, numeroJogos):
    jogo = random.sample(range(1, 61), 6)
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()

for i, v in enumerate(lista, start=1):
    print(f'Jogo {i}: {v}')
    time.sleep(1)
time.sleep(1)
print('----- BOA SORTE -----')
