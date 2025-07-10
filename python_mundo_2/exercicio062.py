#melhora o exercicio 61, pergunta se o usuario quer mostrar mais alguns termos, encerra o programa quando o usuario digitar 0

#exercicio 61
#Refaz o exercício 051, lendo o primeiro termo e a razão de uma P.A  mostrando os 10 primeiros termos da  progressão usando while



print('----- 10 números de uma P.A -----')


termo = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

print('----------------------------------')
cont = 0
while cont <10:
    print('{} → '.format(termo), end='')
    proximoTermo = termo + r
    termo = proximoTermo
    cont += 1

    if cont == 10:
        resposta = 1
        while resposta != 0:
            resposta = int(input('Quer mostra mais termos? Quantos?'))
            c = 0
            while c < resposta:
                print('{} → '.format(termo), end='')
                proximoTermo = termo + r
                termo = proximoTermo
                c += 1
print('ACABOU ESSA PORRA ')      



