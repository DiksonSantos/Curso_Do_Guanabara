'''V_Car =int(input("Digite o Valor do Veiculo:  "))
R = ((V_Car/100)*2)
print("O Valor do Seu IPVA É:{:.3f}" .format(R))'''

'''Origem_Car = float(input('De Onde é a Placa do Veiculo:'))
Coast = int(input('Digite O Valor Do Veiculo:'))
IPV_1=((Coast/100)*4)
IPV_2=((Coast/100)*2)
if Origem_Car =='São Paulo':
    print("O Valor do Seu IPVA É:{:.3f}".format(IPV_1))
if Origem_Car == 'Rio De Janeiro':
    print("O Valor do Seu IPVA É:{:.3f}" .format(IPV_1))
else:
    print('O Valor De Seu IPVA É Apenas:{:.2f}' .format(IPV_2))
'''
#Foi tentado de tudo o que eu sabia no dia ((09-03-18)) Não Deu certo nem Ka Porra (!)

origem = str(input("De Qual Estado é o Veiculo??:"))
valor = float(input('Qual o Valor Atual do Veiculo??:'))
origem_sp = 'São Paulo' #  <- Tente inverter estes valores e ver no que da
origem_rj = 'Rio De Janeiro'
r_1 = ((valor/100)*4+valor)
r_2 = ((valor/100)*2+valor)
if origem == 'São Paulo':
    print('O Valor de Seu IPVA é :{:.3f}'.format(r_1))
elif origem == origem_rj:
    print('O Valohhr Do Teu IPVieA Éeah:{:.3f}'.format(r_2))

