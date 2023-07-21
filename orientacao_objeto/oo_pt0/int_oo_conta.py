#Orientação a Objetos

#Chamamos esse arquivo de int_oo_conta.py como módulo que contém a classe Conta.

class Conta:
    #Damos os nomes de variáveis em OO como referências

    def __init__(self, numero, titular, saldo, limite):  #Função construtor.
        print("Contruindo objeto ... {}".format(self)) # Self é a referência que sabe encontrar o objeto construído na memória

        # próxima linha começará com 'self.' isso implica em a referência levar até o endereço e o . é o comando de ir ao objeto
        #Criamos atributos! Os dois underscores são para que os atributos sejam privados, que não devam ser acessados diretamente
        #Através dos métodos e não fora. Isso é um encapsulamento.
        self.__numero = numero
        self.__titutar = titular
        self.__saldo = saldo
        self.__limite = limite
        #Esse atributos são definimos quando chamamos a classe, como por exemplo: conta = Conta (123, "nico", 55.5, 1000)

    def extrato(self):   #Esse método é chamado no console como <nomeDaVariável>.extrato()
        print("Saldo {} do titular {}".format(self.__saldo, self.__titutar))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #Método que só deixa a forma mais fácil de entender no método saca. __ é para deixar privado
        valor_disponivel_para_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_para_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


    #Esses próximos tipos de métodos são aqueles que somente pegam para trabalhar em outro lugar, são os getters
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titutar

    @property #Para não precisar escrever
    def limite(self):
        return self.__limite

    @staticmethod #Métodos estáticos / da classe  - independe do objeto, é característica, método da classe!
    def codigo_banco():
        return "001"

    @staticmethod #Métodos estáticos / da classe  - independe do objeto, é característica, método da classe!
    def codigos_bancos():
        return "{'BB': '001', 'Caixa': '104', 'Bradesco':'237'}"

    #Esses próximos tipos de métodos são aqueles que alteram os valores dos atributos, chamado de setters
    @limite.setter
    def limite(self, limite):
        self.__limite = limite


#Quando escrevendo o código no console, e queremos achar os atributos da classe do objeto, podemos utilizar o nome do objeto com um ponto na frente: conta.
#Que abrirá uma lista com atributos e possibilidades.

#Atributos são o que o objeto tem, Métodos são o que o objeto sabe fazer, métodos são da classe.