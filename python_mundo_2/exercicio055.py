#Programa que lê o peso de 5 pessoas e mostra qual o maior e qual o menor peso
maiorPeso = 0
menorPeso = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(c)))

    if c == 1:
        menorPeso = peso
        maiorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso



print('O maior peso é {:.1f} e o menor peso é {:.1f}' .format(maiorPeso, menorPeso))

    