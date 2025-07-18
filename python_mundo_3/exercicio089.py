#Programa que lê o nome e duas notas de vários alunos e guarde tudo em uma lista composta, no final mostra um boletim contendo uma média de cada um, e permita que o usuario possa mostra a nota de cada aluno individualmente baseado no nº de indentificação e o programa seja finalizado caso o nº seja maior ou igual a 999.

aluno = []
lista = []
while True: 
    aluno.append(input('Nome: ').capitalize().strip())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))

    lista.append(aluno[:])
    aluno.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Continuar [S/N]? ').strip().upper()
    if continuar in 'N':
        break

print(25*'\033[33m-\033[m')
print(f'{"Nº":<3} {"Nome":<14} {"Média":<6}')
for i, aluno in enumerate(lista):
    media = (aluno[1] + aluno[2])/2
    print(f'\033[33m{i:<4}\033[32m{aluno[0]:<15}{media:<6.1f}\033[m')
print(25*'\033[33m-\033[m')
print('\033[33m----- Notas individuais ------\033[m')
notasIndividuais = 0
while notasIndividuais != 999:
    notasIndividuais = int(input('Mostrar a nota individual de qual aluno? [n°] '))
    if notasIndividuais >= 999:
        break
    if notasIndividuais >= len(lista):
        print('Aluno não encontrado!')
    else:
        for i, aluno in enumerate(lista):
            if notasIndividuais == i:
                print(f'As notas de \033[32m{aluno[0]}\033[m são \033[32m{aluno[1]:.1f}\033[m e \033[32m{aluno[2]:.1f}\033[m!')
print('\033[33m----- Programa finalizado ------ ')
    
