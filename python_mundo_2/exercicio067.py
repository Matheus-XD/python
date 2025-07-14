#Programa que mostre as tabuadas de vários números um de cada vez para cada valor digitado  pelo usuário. O programa será interrompido quando o valor slicitado for negativo
cont = 0

while True:

    print('-------------------------')
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-------------------------')
    
    if n < 0:
        break

    for cont in range(1, 10):
        print(f'{n} X {cont} = {n*cont}')  

print('Programa finalizado!!!')