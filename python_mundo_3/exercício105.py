#Programa que tenha uma função chamada notas que vai receber várias notas de um aluno e vai retornar um dicionário com as seguintes informações: quantidade de notas, a maior nota, a menor nota, a média da turma e a situação (opcional). adicione também o docstring da função

def notas(*n, sit = False):
    """
    -> Função para analisar as notas e situação de um aluno
    :param n: uma ou varias notas de um luno (aceita várias)
    :param sit: valor opcional indicando se deve ou não mostrar a situação do aluno.
    :return: varias informações sobre as notas do aluno
    """
    dicionario = {}

    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    media = sum(n)/len(n)
    dicionario['média'] = media 

    if sit == True: 
        if media > 7: 
            situacao = 'Boa'
        elif media < 5: 
            situacao = 'Ruim'
        else:
            situacao = 'Razoável'
            
        dicionario['situação'] = situacao
    
    return dicionario


resposta = notas(9.5, 3, 4.7, 30, 6, sit=True)
print(resposta)
help(notas)