#Programa que lê o nome e o preço de vários produtos , o programa deve perguntar se o usuário vai continuar. No final mostra
#Qual o total gasto na compra
#Quantos produtos custam mais de R$1000
#Qual é o nome do produto mais barato

print(30*'-')
print('LOJAS MATHEUS')
print(30*'-')

total = maisDeMil = precoMaisBarato = cont = 0
produtoMaisBarato = '' 
while True:

    print('----- PRODUTOS -----')
    produto = input('Nome do Produto: ').strip()
    preco = float(input('Preço: '))
    continuar = ''

    #saber o total gasto na compra
    total += preco

    #saber quantos produtos custam mais de mil
    if preco > 1000:
        maisDeMil += 1
    
    #saber o nome do produto mais barato
    if cont == 0:
        precoMaisBarato = preco  
        cont +=1

    if preco <= precoMaisBarato:
        precoMaisBarato = preco 
        produtoMaisBarato = produto
    
    #saber se quer continuar
    
    while continuar not in 'SN':
        continuar = input('Quer continuar? [ S / N ] ').strip().upper()
    
    if continuar == 'N':
        break

print(30*'-')
print(f'O total da compra foi R${total:.2f}. \nTemos {maisDeMil} produtos custando mais de mil reais. \nO produto mais barato foi {produtoMaisBarato} que custa R${precoMaisBarato:.2f}')
    


