#Desenvolva um programa que leia 4 valores e guarde os em uma tupla, no final mostre: 
#Quantas vezes o valor 9 apareceu
#em qual pocição foi digitado o valor 3
#quais foram os números pares

tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))





print(25*'-')
print(f'O valor 9 aparece {tupla.count(9)} vezes') #count serve para contar quantas vezes o 9 aparece na tupla
if 3 in tupla:
    print(f'O valor 3 aparece na {tupla.index(3) + 1}ª posição') #index serve para mostra a posição que o primeiro 3 aparece na tupla 
else: 
    print('Não há 3 nessa tupla')
    
print('Numeros pares: ', end='')
for c in range (0, len(tupla)):
    if tupla[c] % 2 == 0:
        print(f'{tupla[c]} ', end='')
    