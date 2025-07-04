#Programa que mostra todas as operações basicas dos numeros digitados

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print('RESULTADOS: ')
print('A soma de {} + {} = {}'.format(n1, n2, n1+n2))
print('A subtração de {} - {} = {}'.format(n1, n2, n1-n2))
print('A multiplicação de {} * {} = {}'.format(n1, n2, n1*n2))
print('A divisão de {} / {} = {:.2f}' .format(n1, n2, n1/n2))

#programa que pede um numero e mostra o seu sucessor e antecessor

n = int(input('Digite um numero: '))

a = n - 1
s = n + 1

print('O antecessor de {} é {} e o sucessor é {}'.format(n, a, s))
print('O antecessor de {} é {} e o sucessor é {}'.format(n, (n-1), (n+1)))