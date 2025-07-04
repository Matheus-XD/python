#programa que lê um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#exemplo: 1934 = 4 unidade, 3 dezenha, 9 centena, 1 milhar

numero = int(input('Digite um número entre 0 e 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Análisando o número {}' .format(numero))
print('A unidade é {}' .format(unidade))
print('A dezena é {}' .format(dezena))
print('A centena é {}' .format(centena))
print('O milhar é {}' .format(milhar))