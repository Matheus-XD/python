#Crie um programa que tenha uma tupla única com os nomes de produtos e seus respectivos preços na sequencia, no final mostra uma listagem de preços organizando os dados de forma tabular.

produtos = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo' , 25.00, 'tranferidor', 4.20, 'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)

print(40*'-')
print(f'{"Lista de Preços":^40}')
print(40*'-')

qtdPts = 0

for c in range(0, len(produtos), 2):
    
    qtdPts = 25 - len(produtos[c])
    print(f'{produtos[c]} {qtdPts*'.'} R$ {produtos[c + 1]:.2f}')
        

