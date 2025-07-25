def aumentar(valor = 0, porcentagem = 0, formatado = False):
    """
    função que recebe 3 valores:
    primeiro recebe o valor que sofrerá alteração
    segundo recebe a porcentagem que será acrecentada
    terceiro se receber True mostra o retorno formatado, se receber False ou nada mostra o retorno padrão
    retorna o novo valor após o ajuste
    """
    aumento = valor * (porcentagem/100)
    novoValor = valor + aumento
    return novoValor if formatado == False else moeda(novoValor)

def diminuir(valor = 0, porcentagem = 0, formatado = False):
    """
    função que recebe 3 valores:
    primeiro recebe o valor que sofrerá alteração
    segundo recebe a porcentagem que será diminuida
    terceiro se receber True mostra o retorno formatado, se receber False ou nada mostra o retorno padrão
    retorna o novo valor após o ajuste
    """
    diminuicao = valor * (porcentagem/100)
    novoValor = valor - diminuicao
    return novoValor if formatado == False else moeda(novoValor)

def dobro(valor = 0, formatado = False ): 
    """
    função que recebe 2 valores:
    primeiro recebe um preço
    segundo se receber True mostra o retorno formatado, se receber False ou nada mostra o retorno padrão
    retorna o dobro desse valor
    
    """
    d = valor * 2
    return d if formatado == False else moeda(d)

def metade(valor = 0, formatado = False):
    """
    função que recebe 2 valores :
    primeiro recebe um preço
    segundo se receber True mostra o retorno formatado, se receber False ou nada mostra o retorno padrão
    retorna a metade do valor
    """
    m = valor / 2
    return m if formatado == False else moeda(m)

def moeda(valor = 0, moeda = 'R$'):
    """
    função que recebe 2 valores
    primeiro recebe um preço
    segundo recebe a sigla da moeda desse valor
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(preco, aumento, desconto):
    linha()
    print(f'{"RESUMO DO VALOR":^40}')
    linha()
    print(f'{"Preço analisado:":<30}{moeda(preco):<5}')
    print(f'{"Dobro do preço:":<30}{metade(preco, True):<5}')
    print(f'{"Metade do preço:":<30}{dobro(preco, True):<5}')
    print(f'{"80% de aumento:":<30}{aumentar(preco, aumento, True):<5} ')
    print(f'{"35% desconto:":<30}{diminuir(preco, desconto, True):<5}')
    linha()

def linha():
    print(40*'-')
