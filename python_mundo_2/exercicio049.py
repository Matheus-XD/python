#refaz o exercicio 009 mostrando a tabuada de um numero que o usuario escolher so que agora utilizando um laço for

#Programa que mostra a tabuada do numero que você digitou


n = int(input( 'Digite um número: '))
print('### TABUADA DE {} ####' .format(n))

'''print( '{} X {} = {}' .format( n , 1, n*1))
print( '{} X {} = {}' .format( n , 2, n*2))
print( '{} X {} = {}' .format( n , 3, n*3))
print( '{} X {} = {}' .format( n , 4, n*4))
print( '{} X {} = {}' .format( n , 5, n*5))
print( '{} X {} = {}' .format( n , 6, n*6))
print( '{} X {} = {}' .format( n , 7, n*7))
print( '{} X {} = {}' .format( n , 8, n*8))
print( '{} X {} = {}' .format( n , 9, n*9))
print( '{} X {} = {}' .format( n , 10, n*10))'''

for c in range(1, 11):
    print( '{} X {} = {}' .format( n , c, n*c))

