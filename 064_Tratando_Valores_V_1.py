num = cont = soma = 0 #Resumiu as linhas de baixo
#cont = 0
#soma = 0
num = int(input("Numero: ")) #Assim o numero digitado aqui Não entra nas op matematicas do laço.
while num !=999: #Se o numero a cima for diferente de 999, o laço a baixo sera executado.
    soma = soma + num
    cont += 1 # Contador recebe 1 toda vez que o laço while for executado.
    num = int(input("Numero: ")) #Aqui este mesmo input Tem que ser a Ultima Linha

print("Você Digitou {} Numeros e a soma entre eles foi {}".format(cont, soma))
#print("Você Digitou {} Numeros e a soma entre eles foi {}".format(cont - 1, soma - 999)) #Esta seria outra solução.
