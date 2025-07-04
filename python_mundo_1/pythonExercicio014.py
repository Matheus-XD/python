#Programa que converte de graus celsius para fahrenheit

c = float(input('Digite a temperatura em graus Celsius °C: '))

f = 1.8 * c + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F' .format( c,f))