import math
an = float(input('Digite o angulo que voce deseja:'))
seno = math.sin(math.radians(an))
print('O Angulo {} Tem o Seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O Angulo de {} tem o COSSENO de {:.2f}'.format(an , cosseno))
tangente = math.tan(math.radians(an ))
print('O Ângulo de {} tem a Tangente de {:.3f}'.format(an,tangente))
