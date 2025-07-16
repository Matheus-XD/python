#Crie um programa que o úsuario digite uma expressão qualquer que use parenteses. Seu programa deverá analisar se a expressão passada está correta com os parenteses abertos e fechado na na ordem correta 

expressao = input('Digite a expressão: ')
pilha = 0
for c in range(0, len(expressao)):
    if expressao[c] == '(':
        pilha = pilha + 1
    if expressao[c] == ')':
        pilha = pilha - 1
if pilha == 0:
    print('Expressão valida')
else:
    print('expressão invalida')

não consegui, depois volto aqui quando tiver mais conhecimento


