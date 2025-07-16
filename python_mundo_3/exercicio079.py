#Crie um programa onde o usuário cadastra vários numeros em uma lista, caso o número já esteja lá dentro não será adicionado. No final serão exibidos todos os numeros unicos e em ordem crescente
from time import sleep
lista = []

while True:

    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')

    else: 
        print('Valor duplicado, não adicionado...')

    continuar = ' '
    while continuar not in ['S', 'N']:
        continuar = input('Quer continuar? [S/N] ').strip().upper()

    if continuar == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')






    
