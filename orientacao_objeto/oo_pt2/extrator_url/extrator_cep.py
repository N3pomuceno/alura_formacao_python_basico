import re # Expressões regulares -- RegEx, biblioteca padrão do python para achar ou mexer com strings.

re.compile() 
""" 
Aqui em cima definiremos o padrão que queremos achar dentro de alguma string, 
o compile faz isso e dentro do parênteses a gente define um dígito por uma dupla de colchetes [], e definindo quais caracteres possíveis dentro dele.
como por exemplo para achar um padrão do estilo de CEP (aqui no Brasil):

re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]"), 
caso um caracterer possa aparecer ou não, colocamos um ponto de interrogação para dizer da possibilidade.

É possível armazenar esse compile em uma variável, que seria um Match para a biblioteca, e 
ver se é encontrado em uma string maior.

padrão = re.compile(<formato>)
Tipo = padrão.search(<nome da variável que guarda a string>)
(Se achar ele guarda o endereço que achou e retorna algo, e caso contrário retorna None)
if busca:
    cep = busca.group() - pega o que foi encontrado e coloca na variável cep, ele retorna
    print(cep)

--------------------------------------------------------------------------------------

Para poupar linha na hora de escrever o padrão, podemos ao invés de fazer cada colchetes, podemos utilizar chaves depois que implicariam 
na quantidade de vezes que o dígito se repetiria. 
Além de que dentro do colchetes podemos ao invés de colocar todos, só trabalhar com intervalos, ao invés de 0123456879, só colocar 0-9
exemplo:
re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]"), 
É a mesma coisa que:
re.compile("[0-9]{5}[-]?[0-9]{3}"), 
Interrogação pode ser trocado por {0-1}

"""
