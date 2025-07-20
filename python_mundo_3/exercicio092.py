#Programa que lê o nome, ano de nascimento e número da carteira de trabalho e cadastre-os com idade em um dicionário se por acaso a carteira de trabalho for diferente de 0, o dicionario receberá também o ano de contratação e o salário, calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar (para se aposentar é 35 anos de contribuição)
from datetime import date

pessoa = {}

pessoa['Nome'] = input('Nome: ').capitalize().strip()
pessoa['Data de nascimento'] = int(input('Ano de nascimento: '))
pessoa['Idade'] = date.today().year - pessoa['Data de nascimento']
pessoa['Carteira de trabalho'] = int(input('Carteira de trabalho: '))
if pessoa['Carteira de trabalho'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salario: \033[32mR$\033[m'))
    pessoa['Aposentadoria'] = (pessoa['Ano de contratação'] + 35) - pessoa['Data de nascimento']

print(30*'-')
for k, v in pessoa.items():
    print( f'{k}: R${v:.2f}' if k == 'Salário' else f'{k}: {v}' )
print(30*'-')