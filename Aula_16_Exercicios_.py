#Exercicio 072:
'''
#print("Digite Quit Para Sair")

Num_Strings = ('Zero', "Um", "Dois", "Três", 'Quatro',
               "Cinco", 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:

    Numero = int(input("Digite Numero: ")) # Aqui precisa ser INT para ele usar de Indice.


    #O bloco a baixo é p/ o prog Não dar pau caso digite Numero que não consta no Indice.
    #if 0<= Numero and Numero <= 10: #pARA MIN não fAZ sENTIDO
    if 0< Numero and  Numero <= 10: # Fuleragem....
        break

    print("Try Again")
'''
#for i in range (len(Num_Strings)):

 #   if Numero in Num_Strings[i]:
  #      if Numero == 1:
'''

#Ao Inves de pedir p ele procurar dentro da tupla para então comparar,
#com o metodo a baixo ele tem o numero que for digitado como Indice da Tupla
#e o exibe.

#print("Você Digitou: " + Num_Strings[Numero]) #Usa o numero Digitado Como Indice.
'''

#CONCORDO COM A SOLUÇÃO A BAIXO. AS MOSTRADAS ATÉ MESMO PELO GUANABARA NÃO FAZ SENTIDO P MIN:

extenso = ('zero', 'um', 'dois', 'tres','quatro','cinco','seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
          'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('digite um numero de 0 a 20:: '))
while numero > 20 or numero < 0:
    numero = int(input('numero errrado! digite um numero de 0 a 20 : '))
print(f'O Numero é{extenso[numero]}')



