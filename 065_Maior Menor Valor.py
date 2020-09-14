#29-12-18
'''
cont = 0
soma = 0
entrada = int(input("Digite Um Numero: "))
while entra in "Nn":
    entra = str(input("Quer Continuar? "))
    soma = entrada
    cont = cont +  1
'''

resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite Numero: "))  #MESMO COM DUAS ENTRADAS DENTRO DO LAÇO, ELE MOSTRA UMA POR VEZ (?)
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer Continuar? [S/N] ").upper().strip()[0]) # 0 quer dizer que é pra considerar Só a primeira Letra

media = soma / quant
print("Finish -> Você Digitou {} Numeros, e a Media foi de {}".format(quant,media))
print("O maior Valor foi {} e o menor foi {}".format(maior, menor))
