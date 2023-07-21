#Criação de uma classe filme que terá suas características colocadas num arquivo separado.
import os.path

class Filme:
    def __init__(self, titulo, diretor, nota):
        self.titulo = titulo
        self.diretor = diretor
        self.nota = nota

    def adicionarALista(self):
        lista = open("ListaDeFilmes", "r", encoding="utf-8")
        header = lista.readline()
        linha = lista.readline()
        oFilmeJaEstaNaLista = False
        while linha != "":
            linhaTitulo, linhaDiretor, LinhaNota = linha.split(",")
            if linhaTitulo == self.titulo and linhaDiretor == self.diretor:
                oFilmeJaEstaNaLista = True
            linha = lista.readline()
        lista.close()

        lista = open("ListaDeFilmes", "a", encoding="utf-8")
        if oFilmeJaEstaNaLista != True:
            lista.write("{},{},{}\n".format(self.titulo, self.diretor, self.nota))
        lista.close()

    def __str__(self):
        return "{},{},{}\n".format(self.titulo, self.diretor, self.nota)


def criarLista():
    if os.path.isfile("ListaDeFilmes"):
        print("O arquivo já existe!")
    else:
        lista = open("ListaDeFilmes", "w", encoding="utf8")
        lista.write("Título, Diretor, Nota_0-10\n")
        lista.close()
    return None

#Rodar o arquivo uma vez para criar uma lista, e a partir daí é só entrar no terminal com python3 e ir adicionando novos filmes.
#Se rodar novamente o arquivo, ele irá verificar se o arquivo existe, e caso exista imprimirá uma msg, caso contrário irá criar.

#Forma de só rodar a parte principal se o programa em si for rodado e não importado.
if(__name__ == "__main__"):
    criarLista()
