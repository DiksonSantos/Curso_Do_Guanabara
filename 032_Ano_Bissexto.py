from datetime import date
ano = int(input('Que Ano Quer Analizar? Coloque 0 para Analisar o Ano Atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0:
    '''O Sinal de ! na linha acima significa: 
    Que se o que estiver antes dele(!) for falso, 
    então execute o que estiver depois'''
    '''Ele retorna o contrário da resolução da 
    operação o qual ele precede.
Ou seja:
!true == false
!false == true
!(2 == 2) == false
!(2 == 1) == true'''
    print('O Ano {} É BISSEXTO'.format(ano))
else:
    print('O Ano{} Não É BISSEXTO'.format(ano))
