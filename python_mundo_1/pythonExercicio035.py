#Programa que lê o tamanho de 3 retas e determina se elas podem ou não formar um triângulo

a = float(input('Digite o tamanho da reta A: '))
b = float(input('Digite o tamanho da reta B: '))
c = float(input('Digite o tamanho da reta C: '))

if a + b > c and a + c > b and b + c > a:
    print('As três retas {}, {} e {} podem formar um triângulo!' .format(a, b, c))
else: 
    print('As três retas {}, {} e {} não podem formar um triângulo!' .format(a, b, c))