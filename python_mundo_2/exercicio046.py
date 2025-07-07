#Programa que faz uma contagem regressiva de 10 a 0 para o ano novo com uma pausa de 1 segundo entre os numeros

from time import sleep

print('CONTAGEM REGRESSIVA')
for c in range(10, 0, -1):
    print(c)
    sleep(1)

print('Feliz Ano Novo!!!!')
