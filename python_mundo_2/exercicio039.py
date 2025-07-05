#programa que lê o ano de nascimento de um jovem e informa de acordo com a idade se
#ele ainda vai se alistara no serviço militar, se é hora de se alistar ou se ja passou do tempo,
#O programa também mostra o tempo que falta ou que passou do prazo
from datetime import date 
nascimento = int(input('Digite o ano de nascimento: '))

anoAtual = date.today().year

print('quem nasceu em {} tem {} anos em {}'.format(nascimento, anoAtual - nascimento, anoAtual))

if 2025 - nascimento > 18:
    print('você deveria ter se alistado há {} anos.' .format(anoAtual - (nascimento + 18)))
    print('Seu alistamento foi em {}'.format(nascimento + 18))
elif 2025 - nascimento < 18:
    print('faltam {} anos para o seu alistamento' .format( (nascimento + 18) - anoAtual))
    print(' você deve se alistar em {}' .format( nascimento + 18))
else: 
    print('Você deve se alistar imediatamente')