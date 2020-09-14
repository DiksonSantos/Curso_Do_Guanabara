'''n =str(input('Nome Completo:'))
Maiu = n.upper()
min = n.lower()
Letras = n.split()
Quan = n.count()
Quan_1 = Letras.count(1)
print('Seu Nome em Maiusculo {}\n Em Minusculo {})\n Dividido {}\n Quantidade de Carácteres {}\n Letras da Primeira palavra {}'.format(Maiu, min, Letras, Quan, Quan_1))'''
 #A minha tentativa de solução a cima deu pau na linha 5 -> Eu tentei trabalhar a informação de entrada e mostrar varios resultados dela.
# A baixo vou digitar o codigo do Guanabara.

nome = str(input('Nome Completo:')).strip()
print('Analisando seu nome...')
print('Seu Nome em Maiuscula é: {}'.format(nome.upper()))
print('Seu Nome em Minuscula é: {}'.format(nome.lower()))
print('Seu Nome Tem ao Todo {} Letras'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro Nome Tem {} Letras'.format(nome.find(' ')))
