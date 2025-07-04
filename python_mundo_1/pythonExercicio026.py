#Programa que lê uma frase e mostre:
#quantas vezes aparece a letra A
#Em que posicção ela aparece pela primeira vez
#Em que posição ela aparece pela ultima vez

frase = input('Digite a frase: ')

print('na frase "{}": ' .format(frase.strip().title()))
print('A letra A aparece {} vezes' .format( frase.lower().count('a')))
print('A primeira letra A aparece na posição {}' .format(frase.strip().lower().find('a') + 1)) #frase.find mostra a primeira letra A
print('A última letra A aparece na posição {}' .format(frase.strip().lower().rfind('a') + 1))   #frase.rfind mostra a primeira letra A contando da direita