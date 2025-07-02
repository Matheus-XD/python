#Programa que lê três numeros e mostre qual o maior e qual o menor

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
n3 = int(input('Digite o 3º numero: '))


print('Considerando os numeros {}, {}, {} '.format(n1, n2, n3))
if n1 > n2 and n1 > n3:
    print('{} é o maior numero' .format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior numero' .format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior numero' .format(n3))
if n1 < n2 and n1 < n3:
    print('{} é o menor numero' .format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor numero' .format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor numero' .format(n3))