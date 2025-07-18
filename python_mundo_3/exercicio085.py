#Programa que lê sete valores e cadastre-os em uma lista única que mantenha separados os valores pares e os valores impares, no final mostre os valores pares e valores impares de forma crescente

numeros= [[],[]]

for i in range(0, 7):
    n = int(input(f'Digite o {i + 1}º valor: '))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
        
numeros[0].sort()
numeros[1].sort()

print('\nOs valores pares digitados foram: ', end='')
for i in range(0, len(numeros[0])):
    print(f'\033[32m{numeros[0][i]}\033[m...', end=' ')
print('\nOs valores impares digitados foram: ', end= '')
for i in range(0, len(numeros[1])):
    print(f'\033[32m{numeros[1][i]}\033[m...', end=' ')
print('\n\033[32mPROGRAMA FINALIZADO!\033[m')



