#tira os espaços + joga p\ maiuscula +pegar somente a primeira Letra
sexo = str(input("informe Seu sexo: [M/F] ")).strip().upper()[0]
#idade = int(input("Informe Sua Idade: "))
#print(sexo)
while sexo not in "MF": #No primeiro Input -> Ele jogou tudo p\ Upper para ficar compativel com o que esta aqui nesta String
    sexo = str(input("Dados Invalidos. Por favor Informe o Sexo")).strip().upper()[0]
print("Sexo {} Registrado com Sucesso".format(sexo))

