km = float(input('Kilometros Rodados'))
Days = int(input('Quantos Dias Ficou com o Carro???'))
Press_KM = km * 0.15
R_Days = Days * 60
R_ = R_Days + Press_KM
print('Você Roudou por{}KM\n Durante {} Dias \n O Total a Pagar é: {:.2f}R$'.format(km, Days, R_))
