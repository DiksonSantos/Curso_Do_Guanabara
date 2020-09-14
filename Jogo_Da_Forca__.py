'''palavra_secreta = ['M', 'A', 'C', 'E',  'I', 'O']
Letras_Descobertas = []

print('\n*** Jogo Da Forca ***\n')

for i in range(0, len(palavra_secreta)):
    Letras_Descobertas.append("-")

Acertou = False

while Acertou == False :
    letra = str(input('Digite a letra:'))

    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            Letras_Descobertas[i] = letra

        print(Letras_Descobertas[i])

    Acertou = True

    for x in range(0, len(Letras_Descobertas)):
        if Letras_Descobertas[x] == '-':
            acertou = False'''
#Codigo Não Funcionou . Que mérda