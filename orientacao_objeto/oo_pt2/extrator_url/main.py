
#def 


# Main
url = "  https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"


# Sanitanização dos dados/URL:
url = url.strip()

# Validação da URL: Um detalhe a parte sobre erros: podemos criar, ou levantar um erro para o usuário, meio que forçando ele a acontecer, como a seguinte ideia:
if url == "":
    raise ValueError("A url está vazia!") #Raise é uma forma de levantar uma exceção para mostrar que está dando errado.



# Antes do ponto de interrogação: Base do url.
# Depois do ponto de interrogação: Parâmetros da url.

print(url)

# Separando os dois lados:
url_base, url_parametro = url.split("?")
print(url_base)
print(url_parametro)

# Separando os parâmetros
parametroslista = url_parametro.split("&")
print(parametroslista)
parametros = dict()

for elem in parametroslista:
    nome, dado = elem.split("=")
    parametros[nome] = dado

print(parametros)
