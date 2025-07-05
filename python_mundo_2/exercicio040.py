#programa que lê duas notas e faz a media
#notas menores que 5 é reprovador, entre 5 e 6.9 é recuperação e acima de 7 aprovado 

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/ 2

print('Sua média é {:.1f}!' .format(media))

if media < 5:
    print('Infelizmente vc foi reprovado!!')
elif media >= 5 and media < 7:
    print ('Você está de recuperação!')
else: 
    print('Parabéns, você está aprovado!!!')