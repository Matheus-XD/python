#Programa que Lê o ano de nascimento de uma pessoa e diz sua idade e em qual categoria abaixo ela se encaixa: 
#mirin(até 9 anos), infantil (até 14), junior (até 19), senior (até 20), master (acima de 20)
from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))

idade = date.today().year - nascimento

print('Sua idade é {} anos' .format(idade))
if idade <= 9:
    print('Você está na categoria mirin!')
elif idade > 9 and idade <= 14:
    print('Você está  na categoria infantil!')
elif idade > 14 and idade <= 19:
    print('Você está na categoria junior!')
elif idade > 19 and idade <=20:
    print('Você está na categoria senior!')
else:
    print('Você está na categoria master!')