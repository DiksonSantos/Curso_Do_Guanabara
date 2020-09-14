#Os dois Metodos A Baixo Tem os mesmos Resultados neste problema.

'''for c in range(1,10):
    print(c)
print(("Fim"))
'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')
'''


#_____________________________

#
#for c in range (1, 5):

'''n = 1    #FLAG
while n != 0:    #Com o FOR Isto Não Seria Possível
    n = int(input("Digite Um Valor: "))
print("Fim")
'''

'''
r = "S"
while r == "S": # Enquanto for Digitado S no Input O Laço Continua
    n = int(input("Digite Um Valor: "))
    r = str(input("Que Continuar -> S Ou N ?? ")).upper() #Caso Digite N, ele sai e executa o Print fora do laço.
print("Fim")
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite Um Valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print("Finish!")
print("Você Digitou {} Numeros Pares e {} Numeros Impares".format(par,impar))



# https://www.youtube.com/watch?v=LH6OIn2lBaI&index=26&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye
#28:04 Min  05-12-18
