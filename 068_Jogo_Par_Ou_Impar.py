from random import randint
V = 0
while True: #Tambem chamado de enquanto infinito.
    player = int(input("Diga Um Valor: "))
    comput = randint(0,10)
    tot = player + comput
    TIPO = ' '
    while TIPO not in "PI": #Como foi configurado com UPPER o STR(IMPUT ...
        TIPO = str(input("Par Ou Impar: ")).strip().upper()[0] #0 Significa -> Pegar só a primeira Letra
    print(f"Você Jogou {player} o Computador {comput}. TOTAL -> {tot}")
    print("Deu par" if tot % 2 == 0 else "Deu Impar", end=" ")
    if TIPO == 'P':
        if tot % 2 == 0:
            print("Voce Venceu!")
            V += 1
        else:
            print("Voce Perdeu!")
            break
    elif TIPO == "I":
        if tot % 2 == 1:
            print("Voce Venceu!")
            V += 1
        else:
            print("Você Perdeu")
            break
    print("Vamos Jogar Novamente: ")
print(f"Game Over! Você Venceu {V} Vezes")
