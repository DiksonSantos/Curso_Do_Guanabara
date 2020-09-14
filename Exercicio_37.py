num = int(input("Digite Um Numero Inteiro"))
print('''Escolha uma das bases para concersão:)
[1] converter para Binario
[2] converter para Octal
[3] converter para Hexadecimal''')
opção = int(input("Sua Opção:"))
if opção == 1:
    print('{}Convertido Para Binario é Igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida. Tente Novamente')