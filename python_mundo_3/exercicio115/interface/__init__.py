def linha():
    print(40*'-')

def menu(lista):
    while True:
        linha()
        print(f'{"MENU PRINCIPAL":^40}')
        linha()
        for i in range(len(lista)):
            print(f'\033[33m{i + 1}\033[m - \033[34m{lista[i]}\033[m')     
        linha()
        while True:
            try:
                op = int(input('\033[36mSua opção: \033[m'))
                break
            except:
                print('\033[31mErro: Digite um numero válido\033[m')
        linha()
        return op

        