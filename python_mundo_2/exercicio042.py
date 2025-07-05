#refaz o exercicio035 e acrescenta o recurso de mostrar que tipo de triângulo será formado
#equilatero: todos os lados iguais, isósceles: 2 lados iguais, escaleno: todos os lados diferentes

#exercicio035: Programa que lê o tamanho de 3 retas e determina se elas podem ou não formar um triângulo

a = float(input('Digite o tamanho da reta A: '))
b = float(input('Digite o tamanho da reta B: '))
c = float(input('Digite o tamanho da reta C: '))

if a + b > c and a + c > b and b + c > a:
    print('As três retas {}, {} e {} podem formar um triângulo!' .format(a, b, c))
    if a == b == c:
        print('O triângulo é equilatero: todos os lados são iguais!!')
    elif a == b or a == c or b == c:
        print('O triângulo é isósceles: tem 2 lados iguais!!')
    else: 
        print('O triângulo é escaleno: não tem nenhum lado igual!!')
else: 
    print('As três retas {}, {} e {} não podem formar um triângulo!' .format(a, b, c))


