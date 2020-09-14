frase = str(input('Digite Uma Frase: ')).strip().upper() #Colocou o UPPER Aqui Para não ter problemas com tamanho de letras
palavras = frase.split()
junto = ''.join(palavras) #Este comando junta todas as palavras com o simbolo que estiver (ou não) entre as Aspas
print('Você digitou a frase {} '.format(frase))
print('Frase Juntada {}' .format(junto))
#inverso = ''  # Esta variavel pertense ao esquema do FOR
inverso = junto[::-1] #Ou: O inverso valerá junto do inicio (:) até o fim (:), mas de trás p frente (-1) .Solução usando Fatiamento.
'''for letra in range(len(junto)-1,-1, -1):
    print(junto[letra])
    inverso += junto[letra]'''
# LEN-> Vai até a ultima Letra com o -1.
#Segundo -1 -> Ir até a primeira letra (Que não é Zero e Sim o 1 ou -1). O ultimo -1 Indica que é Pra voltar, ou andar da ultima á primeira.
#Sem o -1 ficaria Ex: em 20 -> do 0 ao 19. Com o -1 ele tira o ZERO e fica do 1 ao 20


print('O Inverso de {} é {}'.format(junto,inverso))
print(inverso)
if inverso == junto:
    print('Temos um Palindromo')
else:
    print('A Frase Digitada Não É Um Palindromo! ')
