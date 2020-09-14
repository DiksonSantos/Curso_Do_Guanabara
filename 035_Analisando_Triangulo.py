comp = float(input('Insira o Segmento A:'))
comp_2 = float(input('Insira o Segmento B:'))
comp_3 = float(input('Insira o Segmento C:'))
if comp < comp_2 + comp_3 and comp_2 < comp + comp_3 and comp_3 < comp + comp_2:
    print('Os Segmentos Acima Podem Formar Um Triangulo!')
else:
    print('Os Segmentos Apresentados Não Podem Formar um triangulo')
