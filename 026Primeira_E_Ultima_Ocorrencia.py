frase = str(input('Digite uma Frase')).upper().strip()
print('A letra A Aparece {} Vezes Na Frase.'.format(frase.count('A')))
print('A Primeira Letra A Apareceu Na Posição {}'.format(frase.find('A')+1))
print('A Ultima Letra A Apareceu na Posição {}'.format(frase.rfind('A')+1))
