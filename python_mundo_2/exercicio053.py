#Programa que lê uma frase qualquer e diz se ela é um palindromo (continua igual escrita de trás para frente) ex: arara 

frase = input('Digite uma frase para saber se é palindromo: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase: "{}" ' .format(junto))
