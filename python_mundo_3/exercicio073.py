#Crie uma tupla com os 20 primeiros times do futebol brasileiro e depois mostrer: os 5 primeiros, os ultimos 4 colocados, times em ordem alfabetica, em que posição está o flamengo

times = ('Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Flamengo', 'internacional', 'Bragantino', 'São Paulo', 'Santo', 'Botafogo', 'Ceará SC', 'Goiáis', 'Avaí', 'Cuibá', 'Coritiba', 'Améria-MG', 'Atlético-GO', 'Fortaleza', 'Juventude')

print(f'Os 5 primeiros times do brasileirão: {times[0:5]}')
print(30*'-')
print(f'Os 4 últimos são {times[-4:]}')
print(30*'-')
print(f'Os times em ordem alfabetica: {sorted(times)}')
print(30*'-')
print(f'O flamengo está na posição {times.index('Flamengo') + 1}')