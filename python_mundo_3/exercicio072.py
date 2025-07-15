#Crie um programa que tenha uma tupla totalmente preenchida com uma contegem por extensão, de 0 até 20. Seu Programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso

extenso = ( 'zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')

while True:

    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break

    print(f'Você digitou o numero {extenso[num]}')
    print()
    
    continuar = ''
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()

    if continuar == 'N':
        break
print('Programa finalizado')


#O programa está correto mas por algum motivo não mostra a pergunta se quero continuar quando execuo o programa