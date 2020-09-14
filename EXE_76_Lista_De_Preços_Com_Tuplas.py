listagem = ['Lapis',1.75, 'Borracha',2, 'Caderno', 15.90, 'Estojo', 25]

print('-'*30)
print(f'{"LISTA DE PREÇOS":^40}') #Formatando Usando 40 Espaços ^ Significa Centralizar.
print('-'*30)

#Percorra a Lista da posição 0 até a extensão total(Len) da Lista
for pos in range(0,len(listagem)):
    #Se a posição for par
    if pos%2 ==0:
        #Mostra/Print a Lista na posição PAR Com 30 Espaços entre o Item na Pos Par e o Item na Pos Impar.
        #Repare no ponto '.' antes do <30  ,que será replicado 30 vezes ao invés dos espaços entre os Itens Pares e Impares.
        # :.<30  -> Contando os caracteres da palavra a ser mostrada, Complete o restante dos 30 Espaços com ...... (pontinhos). Alinhados á Esquerda.
        print(f'{listagem[pos]:.<30}',end='') #O end='' Evita que Os itens Sejam mostrados em Cima de Seus preços.
    else:
        #Imprime das Posições IMPARES da lista Numerais de até 7 digitos Com Duas Casas Depois da Virgula.
        print(f'R${listagem[pos]:>7.2f}')# :>7  -> Espaços entre o R$ e o Digito Final (Contando com todos os Digitos).


#A Direção em que aponta os >  ou <  Indica onde deve estar Posicionado ou Recuado o Item a Ser mostrado/Printado.


'''
#CODIGO REFEITO POR MIN (SOZINHO) DEPOIS DE FAZER OLHANDO, PARA ENTENDER O FUNCIONAMENTO
#ESTA É A ESTRATÉGIA PARA FIXAR O APRENDIZADO:
for pos in range(0, len(listagem)):
    if pos %2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
'''

#EXERCICIO 77 (PRÓXIMO DA PLAYLIST):
#https://www.youtube.com/watch?v=8BgSqrOpKvU&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=7
