#programa que lê o cateto oposto e adjascente de um triângulo e calcule a hipotenusa

from math import hypot
catAdjascente = float(input('Digite o cateto adjascente: '))
catOposto = float(input( 'Digite o cateto oposto: '))

Hipotenusa = hypot(catAdjascente, catOposto) #hypo é uma função da biblioteca math usada para calcular a hipotenusa

print('A hipotenusa desse triangulo é igual a {:.2f}' .format(Hipotenusa))
