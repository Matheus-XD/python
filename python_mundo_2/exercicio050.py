#Programa que lê 6 números inteiros e mostre a soma de apenas aqueles que forem pares, se o valor for impar, desconsidere-o
soma = 0
pares = 0
for c in range(1, 7):
    n = int(input('Digite o {}ª numero: ' .format(c)))
    if n % 2 == 0:
        soma = soma + n
        pares = pares + 1
print('Você informou {} numeros pares \n A soma dos números pares: {} ' .format(pares, soma))
