#Programa que lê um número inteiro e diga se ele é ou não um numero primo, obs: Um numero primo so pode ser dividido duas vezes por 1 e por ele mesmo

total = 0
n = int(input('Digite um número: '))

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print('{}' .format(c), end=' ')
if total == 2: 
    print('O numero {} foi dividido {} vezes, portanto ele é primo' .format(n, total))
else: 
    print('O numero {} foi dividido {} vezes, portanto ele não é primo' .format(n, total))