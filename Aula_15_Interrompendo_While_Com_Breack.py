'''n = cont = 0
while cont <5:
    n = int(input("Digite Numero: "))
    #print(cont,"-> ",end="")
    cont += 1
print("Acabou")
'''

print('Caso queira Parar o Programa Digite 999')

n = s = 0
#while n != 999:
while True:
    n = int(input("Digite um Numero: "))
    #
    if n == 999:
        break
    s += n #agrupar/somar todos os numeros digitados na variavel S  #Esta soma só vai acontecer se 999 for digitado.
#Ou também:
#print("A soma é{}".format(s-999))
#print("A soma é{}".format(s))
print(f"A soma vale {s}") #Novidade de formatação do Python 3.6+ em diante.



#https://www.youtube.com/watch?v=1OFp_-R2B2A&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=36   26inut
