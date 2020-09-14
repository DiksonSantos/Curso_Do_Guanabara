#03-01-18 Aula 15

'''
cont = 0
while cont <= 10:
#while True: #Fará o loop para sempre.
    print(cont, end=" -> ")
    cont += 1
print("FIM")
'''
'''
n = 0
cont = 0
#while cont < 3: # <= 3 aceitaria 4 numeros.
while n != 999:
    n = int(input("Digite Numero: "))
    cont += n
print("A soma é Igual {}".format(cont - 999)) #Dentro do Format é uma gambiarra
'''

'''
n = s = 0
while True:
    n = int(input("Digite Numero"))
    if n == 999: #Para não precisar de gambiarra como no codigo a cima, use o break desta forma.
        break
    s += n
print("(Velho)A Soma Vale %d" %s)  #  %s Para Strings  (Python 2)
print("(ATUAL) A Soma Vale{}".format(s))  #Python 3
print(f"(NOVO) A soma Vale{s}") #Nova forma de usar o print. Python 3.6++
'''

nome = str(input("Nome: ")).strip().capitalize()
idade = int(input("Idade: "))
salario = float(input("Salario: "))
print(f"Funcionario {nome:^8} \nIdade {idade} Anos \nPagamento de: {salario:.3f}R$")
#{nome:8 espaços}
#{nome^20}  -> Centralizar em 20 espaços
#{nome-^30}  -> Centralizar em 30 tracinhos
#{nome->20} Alinhado a Direita com 20 espaços.
