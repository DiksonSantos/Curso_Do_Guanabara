from random import randint
from time import sleep
comp = randint(0,5) # Ele esta randomizando num entre 0 e 5
print ('-=-' *20)
print('Vou Pensar num numero entre 0 e 5. Tente Advinhar...')
print('-=-' * 20)
jogador= int(input('Em que numero eu pensei??')) # Vc vai digitar qualquer numero entre 0 e 5, tentando advinhar qual o PC randomizou
print('PROCESSANDO....')
sleep(2)
if jogador == comp:
    print('PARABÉNS!!! Você Venceu!!')
else:
    print("Haha, Eu Venci")
