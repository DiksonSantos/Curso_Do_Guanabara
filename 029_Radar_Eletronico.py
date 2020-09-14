velo = float(input('Qual Foi A velocidade do Veiculo??:'))
if velo >80:
    print('Você Foi Multado por exceder o Limite de Velocidade')
    multa = (velo-80) * 7
    print('Você Deve Pagar {:.2f}R$'.format(multa))
else:
    print('Tenha Uma Boa Viagem')

