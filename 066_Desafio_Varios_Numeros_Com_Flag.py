# outra maneira equivalente seria s = n = c  Também funcionaria.
s =0
n = 0
c = 0

while True:
    n = int(input("Numero: "))
    if n == 999:
        break
        '''Este bloco de condiçã tem que estar imediatamente apos o INT do qual 
ele vai tratar a informação!'''

    c += 1  #Recebe UM a cada Ciclo
    s += n  #Soma Tudo

print(f"Você Digitou{c} Numeros. A Soma entre eles foi de {s}")

#Proximo Desafio (67):
# https://www.youtube.com/watch?v=X0a5aZg93Uc&index=38&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye
