#Programa que lê o nome de uma cidade e diz se ela começa com "santo" ou não

cidade = input('Digite o nome da cidade: ')

lista = cidade.lower().split()

print('A cidade {} começa com Santo? {}'.format(cidade, 'santo' in lista [0]))

print(lista)