#Programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('So tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Esta totalmente em maiusculo? ', a.isupper())
print('Esta totalmente em minusculo? ', a.islower())
print('Esta capitalizada? ', a.istitle())
