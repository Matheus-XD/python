#Programa que pergunta a quantidade de km rodados por um carro alugado e a quantidade de dias em que ele foi alugado
#e calcula o preço preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por km rodado

quilometrosRodados = float(input('Digite a quantidade de km rodados: '))
diasAlugado = int( input( 'Digite a quantidade de dias alugado: '))

preco = (diasAlugado * 60) + (quilometrosRodados * 0.15)

print('O total a pagar é de R${:.2f}'.format(preco))