#Programa que mostra a area quadrada da parede baseado na altura e largura e a quantidade de tinta
#necessaria para pinta-la tendo em vista que para cada 2m² de parede, um litro de tinta é usado

altura  = float(input( 'Digite a altura da parede em metros: '))
largura  = float(input( 'Digite a largura da parede em metros: '))

area = altura * largura

tinta = area * 0.5

print('Sua parede tem dimensões de {} X {}m e sua area é de {:.2f}m². \npara pinta-la será necessario {:.2f}L de tinta.'.format(altura, largura, area, tinta))
 
