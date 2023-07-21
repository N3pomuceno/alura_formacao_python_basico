import re


class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza(url)
        self.valida_url()

    
    def sanitiza(self,url):          # Esse sanitiza precisa ter como argumento tanto o self, quanto o url, pois se não dá error! Pois quando faz na linha 4 self.sanitiza, o método tá relacionado com self, se não tivesse isso não precisaria.
        if type(url) == str:         # Com esse if, é possível prever casos de None!
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:             # Podemos fazer dessa forma pois se a string url for vazia, seu bool já é identificado como False, mas quando o colocamos o not, faz com que ele entre no if.
            raise ValueError("URL está vazia!")

        # A sequencia desse método é para comparar o padrão com a string url dada, e ver se é uma url válida, isso está de acordo com a biblioteca re (regular extression), que tem mais informações no extrator_cep.py 
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)   #Ao invés de que procurar se uma parte dela se encaixa com o padrão (utilizando o search), utilizaremos o match pois é para ver se é exatamente o que a gente quer. Tem que ver se encaixa com o padrão, mas a string pode ter parte que obedeça ou padrão, não precisa ser inteira.
        if not match:
            raise ValueError("A URL não é válida.")



    def get_url_base(self):
        url_base, extra = self.url.split("?")
        return url_base

    def get_url_parametros(self):
        extra, url_parametros = self.url.split("?")
        url_parametros = url_parametros.split("&")
        return url_parametros
        
    def get_valor_parametros(self, nome_parametro):
        dicio_parametros = dict()
        for elem in self.get_url_parametros():
            nome, dado = elem.split("=")
            dicio_parametros[nome] = dado
        if nome_parametro in list(dicio_parametros.keys()):
            return dicio_parametros[nome_parametro]
        else:
            return None

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        param = ""
        for elem in self.get_url_parametros():
            param += elem + " "
        return self.url + "\n" + "Parâmetros: " + param + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url 



    
    
if (__name__ == "__main__"):
    extrator_url = ExtratorUrl("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
    extrator_url_1 = ExtratorUrl("https://bytebank.com/cambio?moedaOrigem=real&quantidade=1000")
    # extrator_url2 = ExtratorUrl("   ")  - Para verificar se o raise está funcionando!
    # extrator_url3 = ExtratorUrl(None) # - Caso a parte pois None não rege com os mesmos métodos e atributos que string. Ainda chegará numa string vazia e dará error, mas chegamos a algo.
    print(extrator_url.get_valor_parametros("moedaOrigem"))
    print(extrator_url.get_valor_parametros("moedaDestino"))
    print(extrator_url.get_valor_parametros("quantidade"))
    print(extrator_url)

    # EXTRA método dir(classe), mostrará todos os métodos e atributos da classe ou instáncia de classe atribuida.
    # print(dir(str))
    # print(dir(dict))

    print(id(extrator_url)) # id server para ver a identidade do objeto, aonde ele se encontra! Comparar 1 e True serão a mesma coisa, contudo terão id's diferentes. Para comparar a identidade em si precisa utilizar o is!
    # Mais informações sobre is: https://www.alura.com.br/artigos/qual-a-diferenca-entre-e-is-no-python
    print(extrator_url == extrator_url_1)  # Por padrão, se a classe não tem o dunder method de __eq__, essa comparação será de endereços, contudo caso tenha, serão comparados o que a gente quiser.