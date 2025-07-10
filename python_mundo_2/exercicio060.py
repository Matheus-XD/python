#Programa que lê um número qualquer e mostre seu fatorial
#ex: 5! = 5x4x3x2x1 = 120

numero = int(input('Digite um número: '))
cont = numero
fatorial = 1

print('5! = ', end='')
while cont > 0:
    print('{} '.format(cont), end='')
    print('X ' if cont > 1 else '=', end='')

    fatorial = fatorial * cont
    cont -= 1
    
    
print('{}' .format(fatorial))



