def leiaDinheiro():
    valido = False
    while valido != True:
        numero = input('Digite um numero: ').strip().replace(',', '.')
        if numero.isalpha() or numero == '':
            print(f'\033[31mErro! {numero} não é um valor valido\033[m')
        else:
            valido = True
    return float(numero)

