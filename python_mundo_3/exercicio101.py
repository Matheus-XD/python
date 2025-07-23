#Crie uma função chamada voto que receberá por parâmentro o ano de nascimento de uma pessoa. Retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL, ou OBRIGATÓRIO nas eleições

def voto(a):
    from datetime import date
    idade = date.today().year - a
    if idade >= 65 or 16 <= idade < 18:
        return idade, 'OPCIONAL'
    if idade < 18:
        return idade, 'NEGADO'
    else: 
        return idade, 'OBRIGATÓRIO'
            

anoNascimento = int(input('Digite o ano de nascimento: '))
condicao = voto(anoNascimento)
print(f'Com {condicao[0]} anos: VOTO {condicao[1]}!')