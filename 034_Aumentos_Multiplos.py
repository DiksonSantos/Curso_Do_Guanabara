sal = float(input('Digite O Valor do Seu Salário'))
Al_10 = (sal / 100)*10+sal
Al_15 = (sal/100)*15+sal
if sal >= 1250:
    print('Seu Novo SalarioR$ É {:.2f}'.format(Al_10))
if sal <= 1249:
    print('Seu Novo SalarioR$ É: {:.2f}'.format(Al_15))
