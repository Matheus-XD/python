#Programa que tem uma função chamada ficha, que recebe 2 parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deve ser capaz de mostra a ficha do jogador mesmo que algum dado não tenha sido informado corretamente. 

def ficha(j = '', g = 0):
    if j == '':
        j = '<desconhecido>'
    print(f'O jogador {j} fez {g} gol(s) no campeonato')


jogador = input('Jogador: ')
gols = input('Numero de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(jogador,g = gols)

