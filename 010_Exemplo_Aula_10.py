'''nome = str(input('Qual Seu Nome?'))
if nome == "Dikson_":
    print('Que Nome Lindo Você Tem!')
else:
    print('Seu Nome é Tão Normal')
print('Bom Dia, {}'.format(nome))'''

n1 = float(input('Digite a Primeira Nota'))
n2 = float(input('Digite a Segunda Nota'))
n = (n1 + n2)/2
print(' A Sua média foi {:.1f}'.format(n))
if n>=6.0:
    print('Sua Média Foi Boa! PARABÉNS!')
else:
    print('Sua média foi Ruim ESTUDE MAIS')
