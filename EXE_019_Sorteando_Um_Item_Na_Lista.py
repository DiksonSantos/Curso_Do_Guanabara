import random
n1 = str(input('Primeiro Aluno'))
n2 = str(input('Segundo Aluno'))
n3 = str(input('Quarto Aluno'))
n4 = str(input('Quinto Aluno'))
lista = (n1, n2, n3, n4)
escolhido = random.choice(lista)
print('O Aluno Escolhido foi: {} '.format(escolhido))
