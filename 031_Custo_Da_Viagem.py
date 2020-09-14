'''Dist = float(input('Qual é a Distancia da Viagem'))
Res = (Dist * 0.50)
if Dist > 200:
    print (Res)
Res_2 = (Dist * 0.45)
if Dist < 200:
    print (Res_2 )
else:
    print (Res)'''

Dist = float(input('Qual a distancia da viagem??'))
print ('Você Esta Prestes a Começar Uma Viagem de {} KMs'.format(Dist))
if Dist <= 200:
    preço = Dist * 0.50
else:
    preço = Dist * 0.45
print ('O Preço de Sua Passagem Será de{:.2f} R$'.format(preço))
