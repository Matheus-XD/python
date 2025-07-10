#Programa que lê varios numeros inteiros pelo teclado, O programa só vai para quando o usuario digitar o valor 999 que é a condição de parada. No final mostre quantos numeros foram digitados e o valor da soma entre eles

valor = cont = soma = 0

while numero != 999:
    
    numero = int(input('Digite um numero: '))      
    qtd = qtd + 1
    soma = numero + valor
    valor = soma

print('Quantidade de numeros digitados: {} e o valor da soma de todos é igual a {}' .format(qtd - 1, soma - 999))
