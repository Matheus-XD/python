#Programa que calcula a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no intervalo de 1 e 500
soma = 0
quantidade = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
        quantidade = quantidade + 1
        
print('O resultado da soma de todos os {} numeros impares multiplos de 3 entre 1 e 500 é {}' .format(quantidade, soma))