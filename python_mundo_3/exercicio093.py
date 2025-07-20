#Programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou, depois vai ler a quantidade de gols feitos em cada partida. no final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador['Nome'] = input('Nome: ').strip().capitalize()
jogador['Pardidas'] = int(input('Numero de partidas: '))
jogador['Gols'] = []
for i in range(jogador['Pardidas']):
    gol = int(input(f'Quantidade de gols na partida {i + 1}: '))
    jogador['Gols'].append(gol)
jogador['Total'] = sum(jogador['Gols'])

print(30*'-')
print(f'O jogador {jogador["Nome"]} jogou {jogador["Pardidas"]} partidas')
for i in range(jogador['Pardidas']):
    print(f'→ Na {i+1}ª partida fez {jogador["Gols"][i]}')
print(f'O total de gols no campeonato foi {jogador["Total"]} gols')
print(30*'-')