#Crie um programa que tenha uma tupla com várias palavras, depois disso você tem que mostrar para cada palavra quais são as suas vogais


tupla = ('aprender', 'programar', 'liguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for c in range(0, len(tupla)):

    print(f'\nNa palavra {tupla[c].upper()} temos ', end='')
    for letra in tupla[c]:
        if letra in 'aeiou':
            print(letra, end=' ')