a = int(input('Primeiro Numero'))
b = int(input('Segundo Numero'))
c = int(input('Terceiro Valor'))
# O codigo a baixo é para identificar quem é o menor .
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Codigo abaixo é para verificar qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O Menor valor Digitado foi {} '.format(menor))
print('O Maior valor Digitado foi {}'.format(maior))
