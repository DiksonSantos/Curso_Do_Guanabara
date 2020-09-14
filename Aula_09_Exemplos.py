#frase = 'Curso Em Video Python'
#print (frase[9])
'''Neste caso ele apresenta apenas o caractere 9 ( ou seja `V´) Lembrando que começãm em 0, assim contando com os
eapaços o `V´é o nono caractere'''

''' Exemplo de separação da frase ->  frase[9:14]  , com isso ele vai apresentar os caracteres do 9 ao 14, ou seja `Video´
#lembrando que ele não inclui o 14, mas vai até antes dele (Ex: Utilize 9 ao 14 e ele pega até o 13)'''

'''Outro Exemplo de uso é: frase[9:21:2] , onde 9 é o inicio, mostrará até o 20, pois o 21 (se existisse)
 ficaria de fora, e finalmente o 2 que significa Pulando de 2 em 2'''

'''Ex frase:5 ,significa começar do inicio ou 0 até o caractere 5  .  Da mesma forma 15: = do 15 ao final'''

'''Ex: frase[9::3] Significa do 9 ao final, e :3=Pular\mostrar de 3 em três'''

'''len(frase) -> Mostra o comprimento dE frase'''
'''frase.count('o')  -> Conta quantas vezes tem a letra o em frase'''
'''frase.count('o',0,13)  -> significa: do Quantas letras o tem do 0 até antes do
 13 (oucaractere 12)'''

'''frase.find('deo') -> Ele mostrará (neste caso) o 11 que é onde foi encontrado o inicio da 
combinação DEO em frase'''

'''frase.find('Android')  -> Se você coloca em 'find' uma palavra que não existe (no caso em frase)
, ele lhe dará o resultado -1 , que é uma posição que não existe na String'''

''' Função IN ou in Ex: 'Curso in frase --> Significa se existe ou não a palavra ' Curso' em frase'''

#frase = '  Curso Em Video Python  '
#print(frase.replace('Python', 'Android'))
'''Neste exemplo .replace com essa estrutura a
 cima substitui a palavra Python. E caso não haja espaço suficiente na linha o Python
  redimensiona (Ex: de 0 a 20, ele pode aumentar o quanto for necessário'''

'''frase.upper() -> vai deixar tudo em maiusculo, mantendo o
 que já for maiusculo '''

'''frase.lower() -> Deixa tudo em minusculo (no caso tudo o que estiver em frase)'''

'''frase.captalize() -> Deixa só o primeiro caractere em maiusculo, o restante minusculo'''

'''frase.title() -> Transforma todas as primeiras letras de 
cada palavra em Maiuscula'''

'''frase.strip() -> Remove os espaços no inicio e final de
 um campo (quando por exemplo alguem da alguns espaços antes de
  começar a digitar, Para evitar erros por conta disso ,
   esta função retira estes espaços iniciais e final da STRING'''
# Variações de strip -> ex: frase.rstrip()
#    ,  frase.lstrip -> Elimina espaços no inicio Left ou no final da\e frase Right.

'''Divisões:
frase.split()  -> Cada palavra dentro de (Ex:)frase recebe uma
 nova indexação, ou seja Curso=0 ao 4  ,  em=0 e 1  ,Video=0 ao 4
   , Python=0 ao 5.   A Palavra Curso passa a ser 0, em =1 , 
    Video=2, Python=3'''

'''  Ex: '-'.join(frase) -> Junta todo o conteudo de frase (Ou: 0 á20)
   colocando - entre as palavras Ex: Curso-em-Video-Python ou seja 
   20 caracteres contando com o 0 .   Você pode usar qualquer
   coisa no lugar de -, como espaço em branco, ou outros sinais'''

#______________________//______________________









