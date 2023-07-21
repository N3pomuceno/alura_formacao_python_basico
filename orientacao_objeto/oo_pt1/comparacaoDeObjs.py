class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    
    def __str__(self):
        return self.titulo + ' - ' + self.diretor

    def __eq__(self, outro_filme):   # Com esse dunder method é possível fazer a comparação de igualdade e assim comparar se já tem o filme na lista ou não.
        return self.titulo == outro_filme.titulo and self.diretor == outro_filme.diretor


def tenho_o_filme(filme_procurado, lista):
    #meus_filmes = pega_todos_os_filmes()
    # Podemos fazer da forma tradicional, mas ao mesmo tempo temos a forma mais simples que é:
    # for filme in lista:
    #     if filme_procurado == filme:
    #         return True
    # return False
    return filme_procurado in lista


# def pega_todos_os_filmes():
    ## implementação da função que pode ser usada quando pensada em trabalhar com arquivo ou algo do tipo.

movie1 = Filme("A Teoria de Tudo", "James Marsh")
movie2 = Filme("La La Land", "Damien Chazelle")
movie3 = Filme("O Poderoso Chefão", "Francis Ford Copolla")


meus_filmes = [movie1, movie2, movie3]
#meus_filmes = pega_todos_os_filmes()
for filme in meus_filmes:
    print(filme)

filme_procurado = Filme('A Teoria de Tudo', 'James Marsh')

if tenho_o_filme(filme_procurado, meus_filmes):   #Apesar de eu ter visto o filme, a comparação de objeto feita, aparentemente leva a crer que não são a mesma coisa! Isso é antes de colocar o dunder method de equal, que levava a comparação a ser falsa.
    print('Tenho o filme!')
else:
    print('Não tenho :(')


"""
Comparação para python em tipos primitivos:

Os tipos primitivos no python já têm implementado nativamente suas próprias maneiras de se comparar.
No caso do int e da string o que se compara são seus valores.

Para objetos queremos comparar os atributos da classe.
No Python temos como implementar algo similar ao equals(), 
mas ainda mais poderoso - a comparação rica, ou, como é tecnicamente conhecida, rich comparison. 
Com ela, podemos definir os seguintes métodos de comparação em uma classe: desde ==, para != > < >= <=, tem para todos.
    __eq__(), chamado pelo operador ==
    __ne__(), chamado pelo operador !=
    __gt__(), chamado pelo operador >
    __lt__(), chamado pelo operador <
    __ge__(), chamado pelo operador >=
    __le__(), chamado pelo operador <=

Para o que queremos, precisamos da igualdade.
def __eq__(self, outro_filme):
    return self.titulo == outro_filme.titulo and self.diretor == outro_filme.diretor

"""