#Programa que lê um numero quebrado e aredonda-o para baixo usando a função floor da biblioteca math

import math

num = float(input('Digite um número: '))

print('O número digitado foi {} e a sua porção inteira é {}' .format(num, math.floor(num)))