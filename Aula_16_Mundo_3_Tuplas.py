# 09-01-19
from collections import OrderedDict

#Nesta nova vdersão Tuplas podem ser usadas SEM Parenteses:
lanche = ("Burg","Suco",'pizza','Pudim')

#__________________
for La in lanche[0:4]: #Se eu Especificar O Fatiamento na Tupla\Lista etc,
    #..Ele Omite\ Mostra Itens da Tupla.

#Se eu usar o fatiamento no indice, Neste caso La, ele omite\Mostra Letras dos Itens.
    print(La.capitalize() ,end=" - ") #Printa Um Item Por Linha SEM as ASPAS.
    #MAS o ,end=" - " Faz eles Ficarem na mesma Linha

print("\n")
#___________________



print("Indice\Item 3 Da Tupla:\t" + lanche[3])
print(lanche[0:2] , "Mostra todos Os Elementos Antes do Indice 2: Ou 0 & 1")
print(lanche[1:], "Do UM ao Penultimo da Tupla")
print(len(lanche),"  Itens  Na Tupla")
print(lanche[-2] + "-> Penultimo Item ou [-2]")

#lanche = OrderedDict
comida = {"Inhoque"}
#OLHA O QUE EU DESCOBRI !!!!!!!
comida.add(lanche[:]) #COMIDA Recebeu\Concatenou Lanche com Seu Prorpio Conteudo.
#comida = OrderedDict()
print(comida, "+++")

eat = ('Arroz', 'Jaca', 'Maça')

#Para "Concatenar" Tuplas, Ou Add novos valores nelas:
eat = ('Arroz', 'Jaca', 'Maça', 'Soja')
print(eat)

#Continua em:
#  https://youtu.be/q8Z1cRdJnfk?list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH
