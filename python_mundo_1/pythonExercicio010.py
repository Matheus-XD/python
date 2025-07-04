#Programa: Coversor de real para dolar

dolar = float( input( 'Digite o valor do dolar hoje: '))
real = float( input( 'Digite o valor que vc quer converter de R$ para $: '))

realParaDolar = real / dolar

print('R${} vale ${}' .format( real, realParaDolar))