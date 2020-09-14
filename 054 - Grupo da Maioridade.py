from datetime import  date
atual = date.today().year
tot_Maio = 0
tot_Meno = 0
for pess in range(1,8 ): # PESS vai estar no PRINT
#prompt = 'Em que ano A Pessoa Nasceu? : '
    nascimento = int(input('Em que ano A {}º Pessoa Nasceu?'.format(pess)))
    idade = atual - nascimento
    if idade >=21:
        tot_Maio +=1
       # print('Esta Pessoa é Maior de Idade')
    else:
        tot_Meno +=1
print('Ao Todo Tivemos {} Pessoas Maiores de Idade '.format(tot_Maio))
print('E Também Tivemos {} Pessoas Menores de Idade'.format(tot_Meno))
    #print('Esta Pessoa Tem {} Anos'.format(idade))

'''
o FOR e o WHILE são quase Iguais -> A Diferença é que com o for vc cria uma quantidade
de repetições (FOR I in range (1, 12) <- De 1 até 11. Já Com o WHILE , ele 
continua até que a condição seja satisfeita, ou (quando usar uma FLAG ela seja
mudada de TRUE P\ FALSE vice versa).
'''
