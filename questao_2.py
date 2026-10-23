import networkx as nx
import matplotlib.pyplot as plt


VERMELHO = "red"
PRETO = "black"


class No:
    def __init__(self, valor):
        self.valor = valor
        self.cor = VERMELHO
        self.esquerda = None
        self.direita = None
        self.pai = None


class RubroNegra:
    def __init__(self):
        self.raiz = None

    def cor(self, no):
        if no is None:
            return PRETO
        return no.cor

    def rotacao_esquerda(self, x):
        y = x.direita
        x.direita = y.esquerda

        if y.esquerda is not None:
            y.esquerda.pai = x

        y.pai = x.pai

        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y

        y.esquerda = x
        x.pai = y

    def rotacao_direita(self, y):
        x = y.esquerda
        y.esquerda = x.direita

        if x.direita is not None:
            x.direita.pai = y

        x.pai = y.pai

        if y.pai is None:
            self.raiz = x
        elif y == y.pai.direita:
            y.pai.direita = x
        else:
            y.pai.esquerda = x

        x.direita = y
        y.pai = x

    def inserir(self, valor):
        novo = No(valor)

        pai = None
        atual = self.raiz

        while atual is not None:
            pai = atual

            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo.pai = pai

        if pai is None:
            self.raiz = novo
        elif valor < pai.valor:
            pai.esquerda = novo
        else:
            pai.direita = novo

        self.corrigir(novo)

    def corrigir(self, no):
        while (
            no != self.raiz
            and self.cor(no.pai) == VERMELHO
        ):

            avo = no.pai.pai

            if no.pai == avo.esquerda:

                tio = avo.direita

                if self.cor(tio) == VERMELHO:
                    no.pai.cor = PRETO
                    tio.cor = PRETO
                    avo.cor = VERMELHO
                    no = avo

                else:
                    if no == no.pai.direita:
                        no = no.pai
                        self.rotacao_esquerda(no)

                    no.pai.cor = PRETO
                    avo.cor = VERMELHO
                    self.rotacao_direita(avo)

            else:

                tio = avo.esquerda

                if self.cor(tio) == VERMELHO:
                    no.pai.cor = PRETO
                    tio.cor = PRETO
                    avo.cor = VERMELHO
                    no = avo

                else:
                    if no == no.pai.esquerda:
                        no = no.pai
                        self.rotacao_direita(no)

                    no.pai.cor = PRETO
                    avo.cor = VERMELHO
                    self.rotacao_esquerda(avo)

        self.raiz.cor = PRETO


def montar_grafo(no, grafo, pos, cores, x=0, y=0, distancia=6):
    if no is None:
        return

    grafo.add_node(no.valor)
    pos[no.valor] = (x, y)
    cores[no.valor] = no.cor

    if no.esquerda is not None:
        grafo.add_edge(no.valor, no.esquerda.valor)

        montar_grafo(
            no.esquerda,
            grafo,
            pos,
            cores,
            x - distancia,
            y - 1,
            distancia / 2
        )

    if no.direita is not None:
        grafo.add_edge(no.valor, no.direita.valor)

        montar_grafo(
            no.direita,
            grafo,
            pos,
            cores,
            x + distancia,
            y - 1,
            distancia / 2
        )


valores = [
    5, 10, 15, 20, 25,
    30, 35, 40, 45, 50
]

arvore = RubroNegra()

for valor in valores:
    arvore.inserir(valor)


grafo = nx.DiGraph()
pos = {}
cores = {}

montar_grafo(
    arvore.raiz,
    grafo,
    pos,
    cores
)

cores_nos = [
    cores[no]
    for no in grafo.nodes()
]

plt.figure(figsize=(11, 7))

nx.draw(
    grafo,
    pos,
    with_labels=True,
    node_color=cores_nos,
    font_color="white",
    node_size=1800,
    font_size=10,
    font_weight="bold",
    arrows=False
)

plt.title(
    "Questão 2 - Log do Mumbuca - Árvore Rubro-Negra"
)

plt.show()