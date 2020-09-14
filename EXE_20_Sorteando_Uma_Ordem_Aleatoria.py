import random
n1 = (input('Primeiro Aluno'))
n2 = (input('Segundo'))
n3 = (input('Tereceiro'))
n4 = (input('Quarto Aluno'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem Sera:{}'.format(lista))
