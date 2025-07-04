#programa que mostra o dobro, o triplo e a raiz quadrada de um numero digitado

n = int( input( 'Digite um numero: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('Sobre o numero {} \nO dobro é: {}\nO triplo é: {}\nA raiz quadrada é: {}' .format(n, d, t, r))