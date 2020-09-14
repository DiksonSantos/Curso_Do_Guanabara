while True:
    n = int(input("Qual Valor? "))
    if n < 0: #Aqui é a condição que torna FALSE, ou um Numero Negativo
        break
    print("-"*30)
    for c in range (1,11):
        print(f"{n} x {c} = {n*c}")
    print("-"*30)
print("FIM")
