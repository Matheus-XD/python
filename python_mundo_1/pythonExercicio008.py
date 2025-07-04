#Programa que converte uma distancia de metros para quilômetro, hectômetro, decâmetro, metro, decimetro, centimentro, milimetro

m = float( input( 'Digite um numero numero em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * (10**2)
mm= m * (10**3)

print('km: {} \nhm: {} \ndam: {} \nm: {} \ndm: {} \ncm: {} \nmm: {}' .format( km, hm, dam, m, dm, cm, mm))