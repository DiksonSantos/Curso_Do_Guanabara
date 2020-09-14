n = str(input('Digite Seu Nome Completo')).strip()
nome = n.split()
print('Muito Prazer Em Te Conhecer')
print('Seu Primeiro Nome É {}'.format(nome[0]))
print('Seu Ultimo Nome é {}'.format(nome[len(nome)-1]))

''' Como esta descrito ai em cima -> significam na 
linha 4 = Primeiro, 
e na linha 5 = Ultimo'''
