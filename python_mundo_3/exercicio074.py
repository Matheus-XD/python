#Crie um programa que vai gerar 5 números aleatorios, e colocar em uma tupla, depois disso mostre a listagem de números gerados e tabém indique o maior e menor valor que estão na tupla

from random import randint



tupla = (randint(0, 9), randint(0, 9) ,randint(0, 9), randint(0, 9), randint(0, 9))

maior = 0
menor = 0
for c in range(0, len(tupla)):
    #saber qual o maior
    if tupla[c] > maior:
        maior = tupla[c] 
    #saber qual o menor
    if c == 0:
        menor = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]

print(f'Tupla = {tupla}')
print(f'Maior numero: {maior}')
print(f'menor numero: {menor}')

#forma alternativa mais rapido
#dessa forma eu não preciso fazer codigos para saber qual o maior e qual o menor
print(f'Maior numero: {max(tupla)}')
print(f'menor numero: {min(tupla)}')


