#Reescreva a função leia int do desafio 104, incluindo agora a possibilidade da digitação de um numero tipo inválido, aprovei e crie também uma função leiaFloat com a mesma funcionalidade

#Programa que tem uma função chamada leiaInt que funcioná de forma semelha a função input do python mas com uma validação para aceitar apenas valores númericos
def leiaInt():
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
            break
        except:
            print('ERRO!!! O valor digitado  não é um número inteiro')
    return numero
        
def leiaFloat():
    while True:
        try: 
            numero = float(input('Digite um número float: '))
            break
        except:
            print(f'Erro: O valor digitado não é float ')
    return numero

nummeroInt = leiaInt()
numeroFloat = leiaFloat()

print(f'O valor inteiro digitado foi {nummeroInt} e o valor real digitado foi {numeroFloat}')


