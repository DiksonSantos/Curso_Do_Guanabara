palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis",
            "Praticar","futuro","estudar","grátis")

for P in palavras:
    print(f'\nNa palavra {P.upper()} Temos:')
    for Letra in P:
        if Letra.lower() in 'aáãàeéiíóouú':
            print(Letra, end=' ')


#palavra = ((input('Digite uma palavar: ')), (input('Digite uma palavar: ')), (input('Digite uma palavar: ')))
# if letra in 'AEIOU' or letra in 'aeiou':
# #print(letra)
