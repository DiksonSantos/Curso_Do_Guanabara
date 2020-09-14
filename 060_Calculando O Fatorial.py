'''
from math import  factorial
n = int(input("Digite Um Numero Para Fatorial: "))
f = factorial(n)
print("O Fatorial de {} é {}".format(n,f))
'''

n = int(input("Digite Numero: "))
c = n
f = 1
print("Calculando {}!= ".format(n), end="")  # Esclamação Significa Fatorial
while c > 0:
    print("{} ".format(c), end="") # Com END="" Ende Igual á Vazio -> Ele não pula linha P/ Mostrar os Resultados.
    print(" X " if c> 1 else "=", end="")
    f = f * c  # Ou também -> f *= c
    c -= 1
print("{}".format(f))
