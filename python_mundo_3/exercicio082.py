#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares. Ao final, mostre o conteudo das três listas.


lista = []
pares = []
impares = []

while True:   
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    continuar = ' '
    while continuar not in 'NS':
        continuar = input('Dejesa continuar? [S/N] ').strip().upper()
    if continuar in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')