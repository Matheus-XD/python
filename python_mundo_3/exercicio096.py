#Programa que tem uma função chamada área que receba as dimensões de um terreno retângulo (guarde a lagura e comprimento do terreno), e mostre sua área
def area(lar, com): 
    are = lar * com
    print(f'A área de um terreno de {lar:.1f}x{com:.1f} metros é igual a {are}m²!')
def linha():
    print(30*'-')

linha()
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
linha()
area(largura, comprimento)
linha()