#Programa que simula o funcionamento de um caixa eletrônico. No início pergunta ao usuário qual valor será sacado (número inteiro), e o programa vai informar quantas cédulas de cada valor serão entregues.
#Obs: considere que o caixa possui cédulas de R$50, R$20, R$10, R$1


print('----- BANCOS MATHEUS -----')

n = int(input('Valor a ser sacado: \n\033[32mR$\033[m'))
cinquenta = vinte = dez = um = valorRestante = 0


if n % 50 == 0:
    cinquenta = n / 50
else:
    cinquenta = n // 50
    valorRestante = n % 50
if valorRestante % 20 == 0:
    vinte = valorRestante / 20
else:
    vinte = valorRestante // 20
    valorRestante = valorRestante % 20
if valorRestante % 10 == 0:
    dez = valorRestante / 10
else:
    dez = valorRestante // 10
    valorRestante = valorRestante % 10
if valorRestante % 1 == 0:
    um = valorRestante // 1
else:
    um = valorRestante // 1
    valorRestante = valorRestante % 1

print(f'Total de {cinquenta} cédulas de R$50 \nTotal de {vinte} cédulas de R$20 \nTotal de {dez} cédulas de R$10 \nTotal de {um} cédulas de R$1')
