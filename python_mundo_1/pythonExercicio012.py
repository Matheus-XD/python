#Programa que lê o preço de um produto e mostra o novo preço com um desconto de 5%

preco = float( input( 'Digite o antigo preço do produto: '))

novoPreco = preco * 0.95
#ou novoPreco = preco - (preco * 5)/100

print('O produto de R${:.2f} com desconto de 5% fica R${:.2f}' .format(preco, novoPreco))