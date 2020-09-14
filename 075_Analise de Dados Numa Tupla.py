#Metodo para Transformar a Variavel de entrada Numa Tupla
#...eu não conhecia:

num = (int(input("Digite um Numero: ")),
       int(input("Digite Outro Numero: ")),
       int(input("Digite Mais um Numero: ")),
       int(input("Digite um Ultimo Numero: "))
       )

print(f'Você Digitou os Valores {num}') #Aqui ele Printa o NUM como Uma Tupla | Cada Numero numa Linha
print(f'O Valor 9 apareceu {num.count(9)} Vez') #Quando que eu Ia Descobrir este metodo...
if 3 in num:
    #Outro Metodo que eu nem sonhava como se usava:
    print(f'O Valor 3 Apareceu na {num.index(3)}º Posição (Considerando o Zero)')
else:
    print("3 Não Consta Em Nenhuma Posição")
for n in num:
    if n % 2 == 0:
        print(n,": É Numero Par" , end=' ')



#Continua na aula 76: E Depois Já Pular P/ AULA 17
#   https://www.youtube.com/watch?v=Qp2cXfCHk2I&index=7&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH
