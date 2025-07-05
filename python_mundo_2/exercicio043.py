#programa que lê o peso e altura de uma pessoa, calcule o IMC e mostre o status, de acordo com a tabela abaixo
#18.5 ou menos = abaixo do peso, até 25 peso ideal, até 30 sobre peso, até 40 obsidade, acima obsidade mórbida

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso/ (altura * altura)

if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc > 18.5 and imc <= 25:
    print('Você está no peso ideal!!')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso!!')
elif imc > 30 and imc <= 40:
    print('Você está obeso!!!')
else:
    print('Cuidado, Você está com obesidade mórbida!!!!!!')

print('Seu imc é {:.1f}' .format(imc))