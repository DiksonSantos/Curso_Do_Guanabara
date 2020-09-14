'''

'''
somaidade = 0
mEdiaIdade = 0
maiorIdadeHomem = 0
Nome_velho = ''
totMulher20 = 0

for p in range(1,5):
    print('{}º PESSOA'.format(p))
    nome = str(input(('Nome '))).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    print('\n') #Até esta Linha ele Vai fazer as perguntas 4 Vezes - > A partir dai vai começar a trabalhar as informações

    somaidade += idade #
    if p == 1 and sexo in 'Mm': # Ou -> Se a pessoa for a Primeira Pessoa e o Sexo dela for Masculino. # Em frente a SEXO Usar o IN ao Invés de == Faz com que Tanto faz digitar M ou m , ele tem as duas letras ali.
        maiorIdadeHomem = idade # A Variavel MaiorIdade Recebe o numero da variavél IDADE
        Nome_velho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:  #Se a idade deste (proximo) for maior que a do Primeiro, as informações da variavel que vieram do primeiro, serão substituidas pelas deste
        maiorIdadeHomem = idade
        Nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {}'.format(mediaidade))
print('O Homem Mais Velho tem {} Anos se Chama {}'.format(maiorIdadeHomem, Nome_velho))
print('Ao Todo São {} Mulher(es) Com Menos de 20 Anos'.format(totMulher20))







'''
import os

nomes = [] # Armazena os nomes das pessoas
idades = [] # Armazena as idades das pessoas
sexos = [] # Armazena os sexos das pessoas
soma = 0 # Soma as idades das pessoas
maisVelho = 0 # Armazena a idade do homem mais velho
nomeM = '' # Concatena nome e idade do homem mais velho
mSub20 = 0 # Armazena a quantidade de mulheres com idades abaixo de 20 anos
nomeF = '' # Concatena nome e idade das mulheres abaixo de 20 anos
for i in range(0, 4):
    print(str(i+1) + 'ª' + ' pessoa: ')
    nomes.append(input('Nome: ').capitalize())
    idades.append(int(input('Idade: ')))
    sexos.append(input('Sexo(M/F): ').upper())
    soma += idades[i]
    if sexos[i] == 'F' and idades[i] < 20:
        nomeF += nomes[i] + ',' + str(idades[i]) + ' anos; '
        mSub20 += 1

for i in range(0, len(idades)):
    if sexos[i] == 'M' and idades[i] > maisVelho:
        maisVelho = idades[i]
        nomeM = nomes[i]
print('Média de idade do grupo: {:.2f} anos.'.format(soma/4))
print('Homem mais velho: {}, {} anos.'.format(nomeM, maisVelho))
print('Mulheres acima de 20 anos: {}. {}'.format(mSub20, nomeF))﻿
 
'''
