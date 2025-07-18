#aprimora o exercicio anterior mostrando no final:
#a soma de todos os valores digitados
#a soma dos valores da terceira coluna
#o maior valor da segunda linha

linha = []
linhas = []

for li in range(3):
    for co in range(3):
        linha.append(int(input(f'Digite o valor para a posição [{li}, {co}]: ')))
    linhas.append(linha[:])
    linha.clear()

print('\033[33m-----MATRIZ DOS NUMEROS DIGITADOS-----\033[m')
for i in range(0,3):
    for c, v in enumerate(linhas[i]):
        print(f'[ {v:^5} ]', end=' ')
    print()
print(38*'\033[33m-\033[m')
somaPares = somaTerceiraColuna = maior =0
#soma de todos os valores pares
for linha in linhas:
    for valor in linha:
        if valor % 2 == 0:
            somaPares += valor

#soma dos valores da terceira coluna
for i, li in enumerate(linhas):
    for c, co in enumerate(linhas[i]):
        if c == 2:
            somaTerceiraColuna += co
#maior valor da segunda linha
for i, valor in enumerate(linhas[1]):
    if valor > maior:
        maior = valor

print(f'A soma de todos os valores pares é igual a \033[32m{somaPares}\033[m')
print(f'A soma dos valores da terceira coluna é igual a \033[32m{somaTerceiraColuna}\033[m')
print(f'O maior valor da segunda linha é \033[32m{maior}\033[m')

