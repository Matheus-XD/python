#Programa que lê um numero n qualque e mostre na tela os n primeiros elementos de uma sequencia de fibonnaci 
#1,1,2,3,5....

n = int(input('Quantos termos deseja mostrar? '))

cont = 0

natual = 0
nanterior = 0

print('{} → ' .format(0), end='')
while cont < n - 1:

    resultado = natual + nanterior
    nanterior = natual
    natual = resultado

    print('{} → ' .format(resultado), end='')
    
    if natual == 0:
        natual = 1
    
    
    cont +=1
print('FIM!!!')