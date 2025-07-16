#Crie um programa que vai ler vários números e coloque em uma lista, depois disso mostre: quantos números foram digitados, a lista de valores ordenados de forma decrescente, e se o valor 5 está digitado ou não na lista
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').strip().upper()
    if continuar == 'N':
        break

lista.sort(reverse=True)
print(f'A quantidade de numeros digitados foi {len(lista)}')
print(f'Os valores digitados foram {lista}')

#Saber se o valor está na lista
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')

