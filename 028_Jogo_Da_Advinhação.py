from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-' *20)
print('Vou Pensar em Um Numero Entre 0 e 5 Tente Advinhar')
print('-=-' *20)
Jogador = int(input('Em Que Numero eu Pensei'))
print('PROCESSANDO...')
sleep(2)
if Jogador == comp :
    print('PARABÉNS ! Você Conseguiu me Vencer')
else:
    print('GANHEI ! Eu pensei no numero {} e não no {}'.format(comp, Jogador))
