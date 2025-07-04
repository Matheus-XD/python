#Programa que lê um ano qualquer e diz se ele é bissexto 

ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é bissexto ' .format(ano))
        else:
            print('O ano {} não é bissexto'.format(ano))
    else: 
        print('O ano {} é bissexto' .format(ano))
else:
    print('O ano {} não é bissexto' .format(ano))