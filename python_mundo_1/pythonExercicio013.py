#Programa que lê o salário de um funcionário e mostra o novo salário com 15% de aumento

salario = float( input( 'Digite o antigo salario: '))

novoSalario = salario * 1.15

print('O salario de R${:.2f} passa a ser R${:.2f} depois do aumento de 15%'.format(salario, novoSalario))