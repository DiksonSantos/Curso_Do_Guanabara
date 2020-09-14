Maior_Peso = 0
Menor_Peso = 0

for P in range (1,6):
    peso = float(input('Peso da {} Pessoa: '.format(P))) #Com o INPUT Identado, no FOR ele vai aparecer (neste caso) 5 vezes.
    if P == 1: # Se for = 1 -> Indica que este 1 é o peso da primeira pessoa
        Maior_Peso = peso  #Enquanto só tiver o Peso Dela Registrado\Digitado, O Peso dela será o Maior e também será o Menor
        Menor_Peso = peso
    else:
        if peso > Maior_Peso: #Caso contrário -> Se o peso que acabou de ser digitado, for maior do que o Maior peso antes Registrado.
            Maior_Peso = peso # Se o Numero q eu acabei de ler For maior do que o Maior numero que eu tenho o Maior Numero passa a ser o ultimo peso digitado.
        if peso < Menor_Peso:
            Menor_Peso = peso # Se o Peso digitado for menor que o 'MENOR' Peso, o Maior peso passa a ser o 'MENOR'
print('O mairo Peso Lido foi {} Kilos'.format(Maior_Peso))
print('O Menor Peso Lido Foi {} Kilos'.format(Menor_Peso))
