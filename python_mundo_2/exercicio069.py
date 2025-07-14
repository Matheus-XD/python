#Programa que lê a idade e o sexo de varias pessoas, a cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final mostre
#a) Quantas pessoas tem mais de 18 anos
#b) Quantos homens fora cadastrados
#c) Quantas mulheres tem menos de 20 anos

maior = 0
homens = 0
mmv = 0
while True:
    print(25*'-')
    print('CADASTRE UMA PESSOA')
    print(25*'-')

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in ['F', 'M']:
        sexo = input('Sexo: [ M / F ]\n').strip().upper()

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [ S / N ]\n').strip().upper()
    
    #Saber quantas pessoas tem mais de 18
    if idade >= 18:
        maior += 1
    
    #saber quantos homens foram cadastrados
    if sexo == 'M':
        homens += 1
    #saber quantas mulheres tem menos de 20
    if sexo == 'F' and idade < 20:
        mmv += 1

    if continuar == 'N':
        break

    print(30*'-')

print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maior} \nTotal de homens cadastrados: {homens} \nTotal de mulheres com menos de 20 anos: {mmv}')



