'''nasc = int(input("Em que Ano Você Nasceu? :"))
Ano_At = 2018
ida_atu =(nasc - Ano_At)
x_ = 18
menos ='''




from datetime import date
atual = date.today().year
nasc = int(input("Qual Ano De Nascimento:    "))
idade = atual - nasc
print('Quem Nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('voce tem que se alistar imediatamente')
elif idade < 18:
    print('Ainda Faltam{} Anos P Alistameto'.format(saldo))
    ano = atual + saldo
    print('Seu Alistamento Sera em {}'.format(ano))
else:
    saldo = idade - 18
    print('Voce já deveria ter se alistado a {} Anos.'.format(saldo))
    ano = atual - saldo
    print('Seu Alistamento Foi Em: {}'.format(ano))