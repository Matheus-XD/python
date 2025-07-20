#Aprimora o exercício 93 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
jogadores = []
while True:
    jogador = {}
    jogador['Nome'] = input('Nome: ').strip().capitalize()
    jogador['Partidas'] = int(input('Numero de partidas: '))
    jogador['Gols'] = []
    for i in range(jogador['Partidas']):
        gol = int(input(f'Quantidade de gols na partida {i + 1}: '))
        jogador['Gols'].append(gol)
    jogador['Total'] = sum(jogador['Gols'])
    jogadores.append(jogador)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Continuar? ').upper().strip()
    print(30*'-')
    if continuar == 'N':
        break
print(f'{"N°":<7}{"NOME":<20}{"TOTAL DE GOLS":<10}')
for i in range(len(jogadores)):
    print(f'{i + 1:<7}{jogadores[i]["Nome"]:<20}{jogadores[i]["Total"]:^10}')
print()
while True:
    dados = int(input('Mostrar dados de qual jogador? (\033[31mN° do jogador ou 999 para parar\033[m): '))
    if 0 < dados <= len(jogadores):
        for i in range(len(jogadores)):
            if dados == i + 1:
                print(f'Levantamentos do jogador {jogadores[i]["Nome"]}:')
                for c in range(jogadores[i]['Partidas']):
                    print(f'→ Na {c+1}ª partida fez {jogadores[i]["Gols"][c]} gols')
    elif dados == 999:
        break
    else: 
        print ('Digite um valor válido')
    print(30*'-')   
print('----- PROGRAMA FINALIZADO -----') 




