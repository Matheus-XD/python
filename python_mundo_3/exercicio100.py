#Programa que tenha uma lista chamada números e duas funções chamadas sorteia e somaPar, a primeira função vai sortear 5 números e coloca-los dentro da lista, e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior,
from random import randint
from time import sleep
def sorteia():
    for i in range(5):
        n = randint(1, 10)
        numeros.append(n)
def somaPar():
    soma = 0
    for i in range(5):
       if numeros[i] % 2 == 0:
           soma += numeros[i]
    print(f'A soma de todos os números pares foi {soma}')

    
numeros = []
sorteia()
print('Sorteando 5 valores da lista: ', end='')
for i in range(len(numeros)):
    print(f'{numeros[i]}', end=' ', flush=True)
    sleep(0.5)
print()
somaPar()
