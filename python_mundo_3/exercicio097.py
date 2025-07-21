#Programa que tenha a função chamada escreva que receberá um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável 
# ex: ---------
#     Olá mundo
#     ---------

def escreva(msg):
    linha(msg)
    print(msg)
    linha(msg)

def linha(tm):
    print(len(tm) * '-')

mensagem= input('Digite o texto: ')
escreva(mensagem)

