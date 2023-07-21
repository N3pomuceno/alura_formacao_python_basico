from bytebank import Funcionario

#lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)  #Alteramos o segundo parâmetro de inteiro para string, gerou um erro na função

#print(lucas.idade())


# def teste_idade():
#     funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
#     print("Teste = {}".format(funcionario_teste.idade()))


# teste_idade()

ana = Funcionario('Ana', '12/03/1997', 1000)

print(ana.calcular_bonus())