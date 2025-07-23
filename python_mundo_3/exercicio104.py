#Programa que tem uma função chamada leiaInt que funcioná de forma semelha a função input do python mas com uma validação para aceitar apenas valores númericos

def leiaInt(msg):
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[31mERRO! digite um número inteiro valido\033[m')
    return valor

numero = leiaInt('digite um numero: ')
print(f'Você acabou de digitar o valor {numero}')