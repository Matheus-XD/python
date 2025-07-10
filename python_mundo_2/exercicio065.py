#Programa que lê varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todo os valores, qual foi o menor e qual o maior valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
qtd = 0
resultadoAnterior = 0 
soma = 0
maior = 0
menor = 0

while continuar == 'S':
    v = int(input('Digite um valor: '))
    qtd += 1
    soma = soma + v
    resultadoAnterior = soma

    if qtd == 1:
        maior = menor = v

    if v > maior:
        maior = v
    if v < menor:
        menor = v

    continuar = input('Deseja continuar: [ S / N ]').upper().strip()
    
media = soma / qtd
print('Média entre todos os valores {}\nMaior: {}\nMenor: {}'.format(media, maior, menor))