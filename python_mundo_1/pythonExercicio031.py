#Programa que pergunta a distancia de uma viagem em Km e calcula o preço da passagem.
#R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas

distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    preco = distancia * 0.50
    print('O valor da passagem para uma viagem de {}km é R${:.2f}'.format(distancia, preco))
else:
    preco = distancia * 0.45
    print('O valor da passagem para uma viagem de {}km é R${:.2f}'.format(distancia, preco))