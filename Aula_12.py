nome = str(input("Qual é o seu Nome???: "))
if nome == 'Gow Dikson':
    print('Que Nome Wonderful')
elif nome == "Pedro" or nome== 'Maria' or nome== 'Paulo':
    print('Seu Nome é Bem Normal')
elif nome in 'Nana Claudia Jéssica Juliana':
    print('Belo Nome Feminino')
else:
    print('Seu Nome É Bem Comum')
print('Tenha Um bom Dia {}'.format(nome))
