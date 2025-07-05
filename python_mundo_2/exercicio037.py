#Programa que lê um número qualquer e pergunte para que base o usuario pretende converte-lo(binario, octal ou hexadecimal)

n = int(input('Digite um número qualquer: '))
base = int(input('Para qual base vc deseja converter? \nDigite 1 para binário\nDigite 2 para octal\nDigite 3 para hexadecimal\n'))

if base == 1:
    binario = bin(n)
    print('O número {} em binário é {}' .format( n, binario [2:])) #[2:] significa que vai ignorar os 2 primeiros digitos do numero binario e vai começar a mostrar a partir do segundo para frente

elif base == 2:
    octal = oct(n)
    print('O número {} em octal é {}' .format(n, octal[2:]))

elif base == 3:
    hexadecimal = hex(n)
    print('O número {} em hexadecimal é {}' .format(n, hexadecimal[2:]))

else:
    print('Digite um número válido')