#Programa que tenha uma função chamada maior que receba vários parâmentros com valores inteiros, O programa deve analisar todos os valores e dizer qual deles é o maior
from time import sleep
def maior(* num):
    
    maiorValor = 0
    for i in range(len(num)):
        if i == 0:
            maiorValor = i
        else:
            if num[i] > maiorValor:
                maiorValor = num[i]
    print('Analisando os valores passados...')
    for i in range(len(num)):
        print(f'{num[i]} ', end='', flush= True)
        sleep(0.5)
    print(f'\nForam informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maiorValor}')
    print(30*'-')

maior(9, 5, 12, 6, 7, 2)
maior(4, 2, 7, 2, 8, 9, 23, 0)
maior(3, 6, 7, 10)
maior()