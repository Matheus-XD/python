#Programa que lê o salário de um funcionário e calcula o valor do aumento 
#para salários acima de R$1.250,00 o aumento é de 10%
#para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o salário: '))

if salario <= 1250:
    novoSalario = salario * 1.15
    print('O novo salário com 15% de aumento é igual a R${:.2f}' .format(novoSalario))
else:
    novoSalario = salario * 1.1
    print('O novo salário com 10% de aumento é igual a R${:.2f}' .format(novoSalario))