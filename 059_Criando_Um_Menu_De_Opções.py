from time import sleep
n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))
option = 0
while option != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novo Numero
    [5] Sair do Programa
    ''')
    option = int(input("Qual é a Melhor Opçao: "))
    if option == 1:
        soma = n1 + n2
        print("A Soma entre {} + {} é {}".format(n1,n2, soma))
    elif option ==2:
        Mult = n1 * n2
        print("A Multiplicação entre {} x {} é {}".format(n1, n2, Mult))
    elif option ==3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print("Entre {} e {} o Maior Valor é {}".format(n1,n2,maior))
    elif option ==4:
        print("Informe os numeros Novamente:")
        n1 = int(input("Primeiro Valor: "))
        n2 = int(input("Segundo Valor: "))
    elif option ==5:
        print("Fim")
    else:
        print("Opção invalida :/  Tente Novamente :)")
    print("=-="*20)
    sleep(2)
print("Fim Do Programa Volte Sempre! ")
