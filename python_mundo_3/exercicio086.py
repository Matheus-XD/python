#Programa que cria uma matriz 3x3 e preencha com valores lidos pelo teclado, no final mostre a matriz na tela com a formatação correta
linhas= [[],[],[],]
for li in range(0, 3):
    for co in range(0,3):
        linhas[li].append(int(input(f'Digite um valor para a posição [{li}, {co}]: ')))
print('\033[33m-----MATRIZ DOS NUMEROS DIGITADOS-----\033[m')
for i in range(0,3):
    for c, v in enumerate(linhas[i]):
        print(f'[ {v:^5} ]', end=' ')
    print()
print('\n----- PROGRAMA FINALIZADO -----')