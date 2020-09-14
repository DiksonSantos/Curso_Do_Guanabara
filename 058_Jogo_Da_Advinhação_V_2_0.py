from random import  randint
comp = randint(0,10)
print("Sou se PC Pensei E Um Numero entre 0 e 10")
print("Consegue Advinhar qual Foi ??")
Acertou = False
palpites = 0
while not Acertou: #Ou -> Enquanto ACERTOU for FALSE
    jogador = int(input("Qual é o Seu Palpite? "))
    palpites += 1  #palpite = palpite + 1
    if jogador == comp: #Isto Muda a Flag e Para o Laço WHILE
        Acertou = True
    else:
        if jogador < comp:
            print("Mais")
        elif jogador > comp:
            print("Menos... Tente Mais Uma Vez")
print("Acertou com {} Palpites, Parabéns ".format(palpites))
print()
