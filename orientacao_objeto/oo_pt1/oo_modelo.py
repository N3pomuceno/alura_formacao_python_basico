
class Programa:
    def __init__(self, nome, ano): #Dunder methods, aqueles que tem __, tipo init
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self): #outro dunder method, str especial dela é esperado um retorno de um valor como string, que represente o objeto desejado.
        return f'{self._nome} - {self.ano} : {self._likes}'


"""
Para as classes filhas terem acesso aos atributos privados da classe mãe, daria um problema, pois quando temos um atri-
butos com __, na hora de chamar isso ficaria como (_nome da mãe__nome do atributo) só que é por conveção colocar somente
um _ para deixar como aviso para o outro programador que esse atributo tem como interesse em ser privado.

um detalhe interessante é que pressionando CTRL e clicando em super, ou init ou qualquer parâmetro, referência método,
ele nos retorna a origem daquilo que foi clicado e se na origem, mais informações sobre, onde aparece e afins.

"""


class Filme(Programa): #Programa é a mãe do filme, ele recebe toda a herança, atributos e métodos 
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #Inicializador da classe mãe, que chama nome e ano.
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min : {self._likes}'    #Aparentemente quem tem a prioridade é a classe filha na hora de printar. (tanto a classe mãe quanto a filha tem a propriedade de string.)



class Serie(Programa):
    def __init__(self, nome, ano, temporadas): # Forma de usar características da classe mãe, e acrescentar coisa mais específica.
        super().__init__(nome, ano) # O super é para trabalhar em cima da super classe, a mãe, aproveitando o inicializador dela, e seus atributos.
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas : {self._likes}'


class Playlist:   #Usar uma herança que tem a propriedade de iterável
    def __init__(self, nome, programas):  #String e lista.
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):   # Método que torna a classe iterável. Seja possível usar no for.
        return self._programas[item]

    def __len__(self):   # Método que seja possível para a classe ter um size.
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

    # Como estamos com a heraça do lista, não precisamos mais definir o tamanho
    # def tamanho(self):
    #     return len(self.programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
# print(f'{vingadores.nome} : {vingadores.likes}')
print(vingadores.nome)  #Método da classe mãe.

atlanta = Serie("Atlanta", 2018, 2)
# print(f'{atlanta.nome} : {atlanta.likes}')
print(atlanta.nome)     #Método da classe mãe.

tmep = Filme("Todo mundo em pânico", 1999, 100)

demolidor = Serie("Demolidor", 2016, 3)
print()  #Pular a linha no resultado final


vingadores.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()


"""
Quando trabalhando com herança, podemos dizer que as classes filhas são da mesma classe que a classe mãe.
"""

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist : {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:  # Se tivesse herança com list seria só: for programa in playlist_fim_de_semana:
    # FORMA 1 detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas #if numa linha só, vendo se o programa do for tem o atributo has atribute, e dependendo do atributo que tiver retorna outro valor.
    #FORMA 2
    # if hasattr(programa, 'duracao'):
    #     detalhes = programa.duracao
    # else:
    #     detalhes = programa.temporadas

    print(programa)

print()
# Demonstração de que a herança com a list mantém suas características.
# print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')


# Utilizando o repr
# lista = [1, 2, 4, 5]
#
# print(repr(lista))


"""
Python Data Model (Alguns Dunder Methods)

Inicialzação    __init__
Representação   __str__,__repr__
Container, sequência    __contains__, __iter__, __len__, __getitem__
Numéricos   __add__, __sub__, __mul__, __mod__


Podemos utilizar de classes abstratas para descobrir quais dunder methods faltam para poder utilizar a classe
Precisamos saber se há alguma coleção a ser implementada, ou algo a ser reforçado para que a classe 
implemente corretamente, o que será buscado no pacote de coleções.
"""