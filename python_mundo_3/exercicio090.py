#Programa que leia nome e media de um aluno, guardando também a situação em um dicionario, no final mostre a estrutura na tela:
aluno = {}
aluno['nome'] = input('Nome: ').strip().capitalize()
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situação'] = '\033[32mAPROVADO!!!\033[m'
else:
    aluno['situação'] = '\033[31mREPROVADO!!!\033[m'


print(30*'-')
print(f'O nome é {aluno["nome"]}')
print(f'A média é {aluno["media"]:.1f}')
print(f'A situação é {aluno["situação"]}')


print('------ PROGRAMA FINALIZADO -----')