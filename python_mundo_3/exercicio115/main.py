import interface
import arquivo

arq = 'listaNomes.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    menu = ['1  Ver pessoas cadastradas', '2 - Cadastrar nova pessoa', '3 - Sair do sistema']
    opcao = interface.menu(menu)

    if opcao == 1:
        print('primeira opção')
    elif opcao == 2:
        print('segunda opção')
    elif opcao == 3:
        break
    else: 
        print('\033[31mERRO: Digite um dos números do MENU PRINCIPAL\033[m')

print('Programa finalizado!!!')