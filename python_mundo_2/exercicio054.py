#Programa que lê o ano de nascimento de 7 pessoas e no final mostre quantas pessoas ainda não atingira a maioridade e quantas já são maiores


maiores = 0
menores = 0
for c in range(1, 9):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: ' .format(c)))
    if ano + 21 > 2017:
        menores = menores + 1
    else: 
        maiores = maiores + 1

print(50* '=')
print('Das 8 pessoas, {} são maiores de idade e {} são menores' .format(maiores, menores))
