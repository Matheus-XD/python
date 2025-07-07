#Programa que lê o primeiro termo e a razão de uma Progressão aritimetica. no final mostra os 10 peimeiros termos dessa progressão

print(40* '=')
print(10* '', '10 números de uma P.A')
print(40* '=')

pt = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

for c in range(pt , pt + (10 * r), r): 
    print("{} → ".format(c), end='')

print('Acabou!!!', end='')