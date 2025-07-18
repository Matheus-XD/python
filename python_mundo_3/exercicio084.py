#Programa que lê o nome e peso de várias pessoas guardando tudo em uma lista e no final mostre: 
#Quantas pessoas foram cadastradas
#Uma listagem com as pessoas mais pesadas
#uma listagem com as pessoas mais leves

pessoa = []
pessoas = []


while True: 
    pessoa.append(input('Nome: ').strip().capitalize())
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Continuar: [S/N] ').strip().upper()
    if continuar in 'N':
        break

#Descobrir o maior e menor peso
maior = menor = 0
for i, p in enumerate(pessoas):
    if p[1] > maior:
        maior = p[1]

    if i == 0:
        menor = p[1]
    else:
        if p[1] < menor:
            menor = p[1]

print(40*'-')       
print(f'A quantidade de pessoas cadastradas é \033[32m{len(pessoas)}\033[m')
print(f'O maior peso foi {maior:.2f}KG. peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'\033[32m{p[0]}\033[m...', end=' ')
print(f'\nO menor peso foi {menor:.2f}KG. peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'\033[32m{p[0]}\033[m...', end=' ')
print('\n',40*'-') 
print('\033[33mPROGRAMA FINALIZADO!\033[m')
    

    


