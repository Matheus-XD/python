#Programa que lê um número e imprime na tela se ele é par ou inpar

n = int(input('Digite um numero: '))

if n % 2 == 0:
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é inpar' .format(n))