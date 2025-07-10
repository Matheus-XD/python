# programa que lê dois valores e mostra o menu na tela:

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] substituir os numeros
#[ 5 ] sair do programa

# o programa solicita a operação realizada em cada caso
from time import sleep
n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))

c = 0

while c  < 5: 
    print('---------------------------')
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] substituir os numeros\n[ 5 ] sair do programa')
    escolha = int(input('qual operação você deseja? '))
    print('---------------------------')

    if escolha == 1:
        soma = n1 + n2
        print('{} + {} = {}' .format(n1, n2, soma))
    elif escolha == 2:
        multi = n1 * n2
        print('{} X {} = {}' .format(n1, n2, multi ))
    elif escolha == 3:
        if n1 > n2:
            print('{} é maior que {}' .format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}' .format(n2, n1))
        else:
            print('{} e {} são iguais' .format(n1, n2))
    elif escolha == 4:
        novoN1 = int(input('Substituto do 1º numero: '))
        novoN2 = int(input('Substituto do 2º numero: '))
        n1 = novoN1
        n2 = novoN2
    elif escolha == 5:
        c = 5
    else:
        print('Digite um valor válido')
    sleep(1)

print('Programa finalizado')