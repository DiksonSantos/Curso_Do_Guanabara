#0 - 1 - 1 - 2 - 3 - 5 - 8 #Sempre e a soma dos dois ultimos sucessivamente
#Somar os 2 termos anteriores para obter o proximo.
print("-"*30)
print("Sequencia de Fibonacci")
print("--"*16)
n = int(input("Quantos termos você quer mostrar? "))
t_1 = 0
t_2 = 1
print("~"*30)
print("Termos {} -> {} ".format(t_1,t_2), end="->")
cont = 3
while cont <=n:
    t_3 = t_1 + t_2
    print(" ->{} ".format(t_3), end="")
    t_1 = t_2 # t_1 Passa a ser o T_2
    t_2 = t_3 #sucessivamente
    cont += 1
print("\nFIM")


