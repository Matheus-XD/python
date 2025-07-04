#Programa que lê o nome de uma pessoa e diz se tem Silva nele

nome = input('Digite o nome: ')

print('O nome {} tem Silva? {}' .format(nome, ' silva ' in nome.lower().split()))