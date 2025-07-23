#Programa que tenha uma função chamada fatorial que receba 2 parâmetros, o primeiro que receba o número a calcular e o outro chamado show que será o valor lógico opcional indicando se será mostrado ou não na tela o processo de calculo do fatorial
from time import sleep

def fatorial(n, show = False):
    """
    -> Calcula o fatorial de um número. 
    :para n: o número a ser calculado
    :para show: se vai mostrar o processo ou não
    :return: 
    """
    f =  1
    for c in range(n, 0, -1):
        f *= c
    
    print(f'{n}! = ', end='')
    if show == True:
        for c in range(n, 0, -1):            
            print(f'{c} X ' if c != 1 else f'{c} = ', end='', flush=True)
            sleep(0.5)
        print(f)
    else:
        print(f)


fatorial(10, True)
help(fatorial)