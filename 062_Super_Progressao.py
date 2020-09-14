
print('Gerador de PA')
print(78*"=*=")
primeiro = int(input('Primeiro Termo: ')) #VAI SER SOMADO AO SEGUNDO
razão = int(input("Razão PA: ")) #SEGUNDO TERMO VAI SENDO SOMADO A ELE MESMO+ O PRIMEIRO TERMO
termo = primeiro
cont = 1
tot = 0
mais = 10 #A quantidade de termos\numeros que é mostrada quando o usuario comanda.
while mais != 0:
    tot = tot + mais #ou 0 + 10
    while cont <=tot:
        print("{} -> ".format(termo), end="") #eSTE END="" FAZ TUDO APARECER NA MESMA LINHA EM SEQUENCIA, E NÃO UM EM BAIXO DO OUTRO.
        termo += razão
        cont += 1
    print("PAUSA")

    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(tot))
print("Fim")
