#Programa que lê o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista, no final mostra: quantas pessoas foram cadastradas, a média de idade do grupo, uma lista com todas as mulheres e uma lista com todas as pessoas com idade acima da média

pessoa = {}
pessoas = []
total = 0
while True:
    pessoa['Nome'] = input('Nome: ').capitalize().strip()
    pessoa['Sexo'] = ' '
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = input('Sexo [M/F]: ').upper().strip()
    pessoa['Idade'] = int(input('Idade: '))
    continuar = ' '
    pessoas.append(pessoa.copy())
    total += pessoa['Idade']
    while continuar not in 'SN':
        continuar = input('Continuar [S/N]: ').upper().strip()
    if continuar == 'N':
        break
media = total / len(pessoas)

print(30*'-')
print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'A média de idades é igual a {media}')
print('As mulheres cadastradas foram: ', end='')
for i in range(len(pessoas)):
    if pessoas[i]['Sexo'] == 'F':
        print(f'{pessoas[i]['Nome']}...', end=' ')
print('\nLista de pessoas com idade acima da média: ')
for i in range(len(pessoas)):
    if pessoas[i]['Idade'] > media:
        print(f'    → {pessoas[i]['Nome']}',f'do sexo Masculino' if pessoas[i]['Sexo'] == 'M' else 'do sexo Feminino', f'e {pessoas[i]['Idade']} anos de idade')
print('----- PROGRAMA FINALIZADO -----')