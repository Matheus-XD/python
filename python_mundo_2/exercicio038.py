#Escreva um programa que leia 2 números e compare-os mostrando na tela a segunte mensagem
#O primeiro valor é maior
#O segundo valor é menor
#Os dois valores são iguais

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

if v1 > v2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(v1,v2))
elif v1 < v2:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(v2, v1))
else:
    print('Os valores são iguais')