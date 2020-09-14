print(78*"=*=")
print('Gerador de PA')
primeiro = int(input('Primeiro Termo: ')) #VAI SER SOMADO AO SEGUNDO
razão = int(input("Razão PA: ")) #SEGUNDO TERMO VAI SENDO SOMADO A ELE MESMO+ O PRIMEIRO TERMO
termo = primeiro
cont = 1
while cont <=10:
    print("{} -> ".format(termo), end="") #eSTE END="" FAZ TUDO APARECER NA MESMA LINHA EM SEQUENCIA, E NÃO UM EM BAIXO DO OUTRO.
    termo += razão
    cont += 1
print("FIM")
