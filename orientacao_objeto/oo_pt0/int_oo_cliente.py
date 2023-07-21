
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    #Definindo uma propriedade! Basta escrever como se fosse um método, mas não precisa dos parênteses.
    #Continua com a mesma sintax como se tivesse acessando o atributo, mas na verdade está chamando o getter
    @property
    def nome(self): #Getter
        print("Chamando @property nome()!")
        return self.__nome.title() #Retorna a primeira letra Maiuscula e o resto minúscula.

    @nome.setter    #Setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
