#Programa para provar o emprestimo bancario para compra de uma casa, O programa vai perguntar o valor da casa,
#O salario do comprador e em quantos anos ele vai pagar
#Calcula o valor da prestação mensal sabendo que ele não pode exeder 30% do salário ou então o emprestimo será negado.

valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Digite a quantidade de anos que deseja pagar: '))

prestacao = valor / (anos * 12)

porcentagem = (prestacao*100)/salario

if prestacao <= 0.30 * salario:
    print('Compra aprovada, O valor da prestação a ser paga é igual a {:.2f}% do seu salario' .format(porcentagem))
else: 
    print('Emprestimo negado, O valor da prestação a ser paga é igual a {:.2f}% do seu salario ' .format(porcentagem))

    