def aumentar(valor = 0, porcentagem = 0):
    """
    função que recebe 2 valores:
    primeiro recebe o valor que sofrerá alteração
    segundo recebe a porcentagem que será acrecentada
    retorna o novo valor após o ajuste
    """
    aumento = valor * (porcentagem/100)
    novoValor = valor + aumento
    return novoValor

def diminuir(valor = 0, porcentagem = 0):
    """
    função que recebe 2 valores:
    primeiro recebe o valor que sofrerá alteração
    segundo recebe a porcentagem que será diminuida
    retorna o novo valor após o ajuste
    """
    diminuicao = valor * (porcentagem/100)
    novoValor = valor - diminuicao
    return novoValor

def dobro(valor = 0 ): 
    """
    função que recebe 1 valor:
    retorna o dobro desse valor
    """
    d = valor * 2
    return d

def metade(valor = 0):
    """
    função que recebe 1 valor:
    retorna a metade do valor
    """
    m = valor / 2
    return m

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
    
