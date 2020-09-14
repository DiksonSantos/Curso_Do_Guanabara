num = int(input('Digite Numero: '))
tot = 0 #Esta variavel é para guardar\exibir a quantidade de numeros Divisiveis
for I in range(1,num + 1):  # De 1 até o numero que for digitado + 1 (porque +1, caso contrario ele para Um Num Antews)
    if num % I == 0: # Significa -> Se o Numero for divisivel pelo contador que neste caso é I
        print('\033[33m') # Isso são codigos de cores  (\33...
        tot += 1
    else:
        print('\033[31m', end='') # Fica Amarelo
    print('{} '.format(I), end='') # Se não => Numero fica Vermelho ->O I esta com o Codigo \033[33m(Ou Vermelho)

#Os Comandos A Baixo jão não fazem parte do Laço a cima:
print('\n\033[m0 numero {} Foi Divisível {} Vezes (Numeros Que estão Em Amarelo) '
      .format(num,tot)) #\033[m0 -> É um codigo P\ Zerar a Cor.
if tot == 2: # Ou Se TOT for Divisivel Por Apenas 2 Numeros (O que Configura\quer dizer que é Um Numero Primo)
    print('E Por Isso Ele É Primo! ')
else:
    print('E Por Isso ele NÃO É Primo')

#Numeros Primos Só podem Ser Divididos por eles Mesmo e Por 1 

'''No exer do Guanabara ele mostra todos os numeros (Print) Numa linha só, aqui eles 
foram exibidos um embaixo do outro com apenas os numeros que não dividem o numero que vc digita aparencendo em linha 
e em outra cor'''

# Video 53 ->  https://www.youtube.com/watch?v=5VBWe6BXzRo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=22
