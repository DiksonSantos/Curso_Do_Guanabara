
soma = 0
contador = 0
for numero in range(1,7): #De Um ao Sete (Na verdade 6)
    num = int(input('Digite {}º Numero: '.format(numero))) #Vai Ler 6X a Variavel NUM
    if num % 2 == 0: #Isso quer dizer que ele só vai somar se os numeros forem Pares.
        soma = soma + num # Ou variavel soma += Var num
        contador = contador + 1 #Ou contador += 1
print('Você Informou {} Numeros Pares, e a Soma Deles Foi {}'.format(contador,soma))

'''
# Explicando Para que serve o % Em Python -> Para saber se um numero é par ou Impar:
num = input("Digite um número: ")
if(num % 2 == 0):
    print("Número par.")
else:
    print("Número ímpar")

#Ou if(num % 2 !=0):
    print('Numero Impar)  -> Pois numeros divididos com resto Diferente de 0 Não
    são Pares como-> 3/2 = 1,50 (resto=0,50=numero Impar) 
_____________________________
No código acima, pedimos para o usuário digitar um número. Em seguida, 
armazenamos esse número na variável de nome num. Feito isso, 
obtemos o módulo de num por 2. Caso o valor retornado seja diferente de 0,
 a divisão não é inteira, logo o número não é par. Em seguida, 
 imprimimos no Console a frase dizendo se o valor digitado é ou não par.
'''
