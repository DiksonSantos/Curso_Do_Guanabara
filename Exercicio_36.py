V_Home = float(input("Qual O Valor Da Casa??:  R$"))
sal = float(input("QUal O Seu Salário?:"))
year = int(input("Pagará Em Quantos Anos?:"))
min = sal *30/100
presta = V_Home / (year*12)
print('Para Pagar uma casa de R${:.2f} em {} anos' .format(V_Home, year), end ='')
print( ' a prestação será de R${:.2f}' .format(presta))

print (' Comparando tem que pagar {} e o minimo é de {}'.format(presta, min))
if presta <= min:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo Negado')
