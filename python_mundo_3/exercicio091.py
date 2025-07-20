#Programa onde 4 jogadores jogam um dado e tem resultados aleatorios, guarde esse resultado em um dicionario, no final coloque esse dicionário em ordem, sabendo que no final o vencedor tirou o maior número no dado
from random import randint
from time import sleep
from operator import itemgetter

resultados = {
    'jogador 1': randint(1,6), 
    'jogador 2': randint(1,6), 
    'jogador 3': randint(1,6), 
    'jogador 4': randint(1,6)
}

print('----- VALORES SORTEADOS ----- ')
for k, v in resultados.items():
    print(f'{k} tirou {v}')
    sleep(0.5)

ranking = []
ranking = sorted(resultados.items(), key= itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
    print(f'{k+1}º clocado: {v[0]} com {v[1]}')


