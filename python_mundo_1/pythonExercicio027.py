 #Programa que lê o nome completo de uma pessoa e mostre o primeiro e ultimo nome dessa pessoa

nome = input('Digite o nome: ').strip()

lista = nome.split()
print('O primeiro nome é {} e o ultimo é {}' .format(lista [0], lista[len(lista) - 1]))