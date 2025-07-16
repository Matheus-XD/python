#Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

maior = maiorPosicao = menor = menorPosicao =  0

for c, v in enumerate(lista):
    
    if v > maior:
        maior = v
    
    if c == 0:
        menor = v
    
    if v <= menor:
        menor = v

print(40*'-')
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição: ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c}... ', end='') 

print(f'\nO menor valor digitado foi {menor} na posição: ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}... ', end='')
