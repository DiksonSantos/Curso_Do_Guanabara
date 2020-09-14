num = 0
cont = 0
soma = 0

num = int(input("Digite 999 Para Parar_: "))#Mostrado Apenas na primeira Linha

while num != 999:

    soma = soma + num #Armazena E Soma todos os numeros digitados.
    cont += 1 #Referente á quantidade de vezes que vc digitou algo
    num = int(input("Digite 999 Para Parar: "))#O restante das Linha de entrada serão assim.

#print("Você Digitou {} Numeros e a soma entre eles foi {}".format(cont -1,soma - 999))
print("Você Digitou {} Numeros e a soma entre eles foi {}".format(cont ,soma ))
