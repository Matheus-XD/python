#Programa que lê nome idade e sexo de 4 pessoas e mostre a media de idades do grupo, o nome do homem mais velho e quantas mulher tem menos de 21 anos
somaidades = 0
maiorIdadeMasculino = 0
maiorIdadeMasculinoNome = ''
qtdMulheresMenos21 = 0

for c in range(1, 5): 
    print('----- {}ª PESSOA -----' .format(c))
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Qual o sexo? [ M/F ]: ').lower().strip()

    somaidades  = somaidades + idade

    if sexo == 'm' and idade > maiorIdadeMasculino:
        maiorIdadeMasculino = idade
        maiorIdadeMasculinoNome = nome

    if sexo == 'f' and idade < 21:
        qtdMulheresMenos21 = qtdMulheresMenos21 + 1

media = somaidades/4

print('A média de idades é {} \nO homem mais velho se chama {} e tem {} anos. \nTem {} mulheres com menos de 21 anos' .format(media, maiorIdadeMasculinoNome, maiorIdadeMasculino, qtdMulheresMenos21))