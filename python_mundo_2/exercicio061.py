#Refaz o exercício 051, lendo o primeiro termo e a razão de uma P.A  mostrando os 10 primeiros termos da  progressão usando while

#exercicio 051
#Programa que lê o primeiro termo e a razão de uma Progressão aritimetica. no final mostra os 10 peimeiros termos dessa progressão

print(40* '=')
print(10* '', '10 números de uma P.A')
print(40* '=')

termo = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))


print('------ Usando FOR ------')
for c in range(termo , termo + (10 * r), r): 
    print("{} → ".format(c), end='')

print('Acabou!!!')

print('------ Usando WHILE ------')
cont = 0
while cont < 10:
    print('{} → '.format(termo), end='')
    proximoTermo = termo + r
    termo = proximoTermo
    cont += 1
print('Acabou!!!')

     