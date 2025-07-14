#Programa que lê vários numeros pelo teclado, O programa só vai parar quand o usuário digitar 999, no final mostra quantos numeros digitados e qual o valor da soma entre eles(desconsiderando o flag 999)

soma = cont = 0

while True:
    num = int(input('Digite um número: '))

    if num == 999:
        break
    
    cont += 1
    soma = soma + num


print(f'A soma dos {cont} valores é igual a {soma}')



