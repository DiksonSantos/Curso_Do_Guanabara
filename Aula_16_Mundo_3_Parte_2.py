from collections import  OrderedDict # Só serve Para Dic tipo 'Chave:Item'

lanche = ("Burg","Salgado",'pizza','Pudim','gelatina')
for cont in range(0, len(lanche)):#Variavel CONT vai de 0 até o Comprimento de Lanche
#CONT Vai percorrendo Lanche Ok, então cada item de lanche é CONT. Vai ser reetido
#..conforme a quantidade de itens de Lanche.
    print(lanche[cont], end=" - ") #Mostra Qual o lanche na posição CONT

#Outra maneira Logo a baixo:

print("\n")
#lanche = ("Burg","Salgado",'pizza','Pudim','gelatina')
for comida in lanche:
    print("Eu Comi: ", comida.capitalize())
    #print(f'Eu Como: {comida.upper()}', end="-")

#Novidade:
print("\n")
for pos, comida in enumerate(lanche):
    print(f"Comendo: {comida} Item-> { pos}")
print(sorted(lanche)) #Diz que poe em ordem, mas aqui bagunçou tudo a ordem.

Num = (5,2,4,9,1)
Nume_2 = (0,3,8,7,6,0)
C = Nume_2 + Num
#Mas Para Numeros Parece que funcionou perfeitamente na ordenação
print( sorted(C),"Quant de Nums:" ,len(C)) #Juntou e Ordenou as Duas Tuplas.
print("Quantas vezes aparece 0 Na tupla? ",C.count(0))
print("Em que Posição esta o 7 nestas Tuplas: ",C.index(7))

Mixed = ('Gow', 32, 'Masc')
for m in Mixed:
    print(m, end="-")
#del(Mixed) #Esta linha Impede a linha de baixo de ser Exibida\Mostrada.
print("\n" , Mixed)

#Continuar em 43:27Min (Desafios)
# https://www.youtube.com/watch?v=0LB3FSfjvao&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH

