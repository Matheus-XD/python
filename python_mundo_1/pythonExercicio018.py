#Programa que lê um valor na tela e mostra o valor do Seno, Cosseno, Tangente desse ângulo

import math 

angulo = float(input( 'Digite um ângulo: '))

anguloEmRadianus = math.radians(angulo) #para calcular sen, cos e tan o angulo precisa tá no formato radianus
seno = math.sin(anguloEmRadianus)
cosseno = math.cos(anguloEmRadianus)
tangente = math.tan(anguloEmRadianus)

print('Ângulo: {}\nSeno: {:.2f}\nCosseno: {:.2f} \nTangente: {:.2f}' .format( angulo, seno, cosseno, tangente))