#Programa que lê a velocidade de um carro, se passar de 80km/h imprime a mensagem de que ele foi multado e
#o valor da multa (R$7,00 para cada km acima do limite de velocidade)

velocidade = float(input('Digite a velocidade: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado no valor de R${:.2f} por andar {:.1f}km/h acima do limite de velocidade de 80km/h' .format(multa, velocidade - 80))
