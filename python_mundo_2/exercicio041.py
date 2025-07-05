#Programa que Lê a idade de uma pessoa e diz se ela está nas categorias: 
#mirin(até 9 anos), infantil (até 14), junior (até 19), senior (até 20), master (acima de 20)

idade = int(input('Digite a sua idade: '))

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