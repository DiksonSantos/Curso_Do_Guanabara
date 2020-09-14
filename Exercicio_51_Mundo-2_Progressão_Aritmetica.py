prim = int(input('First Term: '))
razão = int(input('Razão: '))
décimo = prim + (10 - 1) * razão
for c in range(prim,décimo + razão ,razão):
    print('{} '.format(c), end='-> ') #The end=' ' is just to say that you want a space after the end of the statement instead of a new line character. In Python 2.x you would have to do this by placing a comma at the end of the print statement. The end parameter means that the line gets ' ' at the end rather than a newline character.
print('ACABOU')

#Legal, mas não entendi o funcionamento pois não sei ainda Progressão Aritmetica (Preciso aprender).
