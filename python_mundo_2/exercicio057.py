#Programa que lê o sexo de uma pessoa mas só aceite os valores de M e F, caso o valor esteja errado, peça a digitação novamente até está correto

sexo = str(input('Digite o seu sexo: [ M / F]\n')).upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    print('##### ERRO ######')
    novoSexo = str(input('Digite um valor correto: [ M / F ]\n')).upper().strip()
    sexo = novoSexo

if sexo == 'M':
    print('Entendido, você é um homem')
else:
    print('Entendido, você é uma mulher')

print('Fim')
