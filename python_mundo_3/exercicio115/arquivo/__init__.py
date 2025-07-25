import os

def arquivoExiste(nome):
    try:
        os.chdir(r"C:\Users\Mathe\Desktop\Python\cursoGuanabara\python\python_mundo_3\exercicio115")
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        os.chdir(r"C:\Users\Mathe\Desktop\Python\cursoGuanabara\python\python_mundo_3\exercicio115")
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else: 
        print(f'Arquivo {nome} criado com sucesso')