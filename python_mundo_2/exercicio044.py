#programa que calcula o valor a ser pago por um produto considerando seu preço normal e a forma de pagamento,
#À vista ou cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#Em 3x or mais: 20% de juros

valor = float(input('Digite o valor do produto: '))

pagamento = int(input('Forma de pagamento\nDigite 1 para á vista ou cheque\nDigite 2 para á vista no cartão\nDigite 3 para parcelar em até 2x\nDigite 4 para parcelar em 3x ou mais\n'))

if pagamento == 1:
    valorFinal = valor * 0.9
    print('O produto a vista ou cheque fica no valor de R${:.2f} com 10% de desconto' .format(valorFinal))
elif pagamento == 2:
    valorFinal = valor * 0.95
    print('O produto a vista no cartão fica no valor de R${:.2f} com um 5% de desconto' .format(valorFinal))
elif pagamento == 3:
    valorFinal = valor
    print('O produto parcelado em 2x no cartão fica no valor normal de R${:.2f}' .format(valorFinal))
elif pagamento == 4:
    valorFinal = valor * 1.2
    print('O produto parcelado em 3x ou mais fica no valor de R${:.2f} com 20% de juros' .format(valorFinal))
else:
    print('Digite uma forma de pagamento válida')

