#Crie um modulo camado moedas.py que tenha as funções incorporadas aumentar() diminuir() dobro() e metade() faça também um programa que importe esses modulos e use algumas funções


import moedas
p = float(input('Digite um preço: R$'))

print(f'A metade do preço {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro do preço {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentado de 10%, temos {moedas.moeda(moedas.aumentar(p, 10))} ')
print(f'Diminuindo 13%, temos {moedas.moeda(moedas.diminuir(p, 13))}')