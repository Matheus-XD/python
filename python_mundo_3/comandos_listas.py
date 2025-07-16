#lista
num = [2, 5 , 9 , 1]

#troca o numero no indece 2 por 10
num[2] = 10

#adiciona o numero 13 no final lista
num.append(13)

#organiza os valores em ordem crescente ou alfabetica
num.sort()

#organiza de forma reversa 
num.sort(reverse=True)

#inserer 3 na posição 0 e todo os que estão depois são afastados uma casa para frente
num.insert(0, 3)

#deleta o numero que está na posição 1
del num[1]

#deleta o ultimo numero da lista
num.pop()

#remove o numero 2 da lista (remove apenas o primeiro)
num.remove(2)

#Ler valores
lista = []

for c in range(0, 5):
    lista.append( int(input('Digite um valor: ')))

for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}!!!')

print('Fim da lista!!!')