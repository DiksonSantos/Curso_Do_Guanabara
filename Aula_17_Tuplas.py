lanches = ['Hot_dog', 'Burger', 'Juice', 'Pizza', 'IceCream', 'Cookie','Burger']
print(lanches) #Lista completa

del(lanches[3])
print(lanches) #Lista sem a PIZZA (Pos 03)

X = lanches.pop(3)
print(X) #Item deletado/Guardado Pelo POP
print(lanches)#Sem o Sorvete

lanches.remove('Cookie')
print(lanches)# Sem o Item especificado na Lista

#Para evitar bugs na hora de remover:
if 'Juice' in lanches:
    lanches.remove('Juice')
    print(lanches)
else:
    print('Não Achei Nada')

Val = list(range(0,6,2))
y = tuple(Val)
print(y)

lanches.insert(0, "Manga") #Abriu esoaço para por Manga
print(lanches)

lanches.remove('Burger') #Removeu a  PRIMEIRA OCORRENCIA de Burger
print(lanches)

'''
for I, J in enumerate(y):
    print(f'Na posição {I} Encontrei {J}', end='-')
'''

Valores = []
for cont in range(0,3):
    Valores.append(int(input("Digite Valor: ")))
    Valores.sort()
print(Valores)

B = tuple(Valores.copy())
C = B[:]

print(B)
print('\n')
print(C)


#CONTINUA EM:
#https://www.youtube.com/watch?v=q8Z1cRdJnfk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=9
