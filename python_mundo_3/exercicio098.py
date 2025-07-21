#Programa que tenha uma função chamada contador que receba 3 parâmetros: inicio, fim e passos, e realize a contagem. O programa deve realizar 3 contagens através da função criada:
#a) de 0 a 10 de 1 em 1
#b) de 10 a 0 de 2 em 2
#c) uma contagem personalizada
from time import sleep
def contador(inicio, fim, passos):
    li = []
    if passos == 0:
        passos = 1

    if inicio > fim or passos < 0:
         passos *=  -1

    for i in range(inicio, fim + passos if inicio < fim else fim + passos , passos):
            li.append(i)
    if passos < 0: 
         passos *= -1

    print(f'Contagems de {inicio} até {fim} de {passos} em {passos} ')
    for i in range(len(li)):
        print(f'{li[i]}',end=' ', flush= True)
        sleep(0.5)
    print()
    print(30*'-')
        
contador(0, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passos = int(input('Passos: '))
contador(inicio, fim, passos)
