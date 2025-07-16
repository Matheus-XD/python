#Crie um programa onde o usuário pode digitar 5 valores e cadastre os em uma lista já na posição certa de inserção (sem usar sort()) no final mostra a lista ordenada na tela

lista = []

for c in range(0, 5):

    num = int(input('Digite um número: '))

    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Valor adicionado no final da fila...')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Valor adicionado na posição {posicao}')
                break
            posicao += 1


print(f'{lista}')




