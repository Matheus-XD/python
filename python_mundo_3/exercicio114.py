import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print('\033[31mInfelizmente o site pudim não está funcionando!!!\033[m')
else:
    print('\033[32mO site pudim está funcionando perfeitamente!!!\033[m')