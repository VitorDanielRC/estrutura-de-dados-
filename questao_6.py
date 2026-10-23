import networkx as nx
import matplotlib.pyplot as plt


RED, BLACK = 0, 1


class No:
    def __init__(self, chave):
        self.chave = chave
        self.cor = RED
        self.esq = None
        self.dir = None
        self.pai = None


class ArvoreRubroNegra:
    def __init__(self):
        self.NIL = No(None)
        self.NIL.cor = BLACK
        self.NIL.esq = self.NIL
        self.NIL.dir = self.NIL

        self.raiz = self.NIL

    def _rot_esq(self, x):
        y = x.dir
        x.dir = y.esq

        if y.esq != self.NIL:
            y.esq.pai = x

        y.pai = x.pai

        if x.pai is None:
            self.raiz = y

        elif x == x.pai.esq:
            x.pai.esq = y

        else:
            x.pai.dir = y

        y.esq = x
        x.pai = y

    def _rot_dir(self, y):
        x = y.esq
        y.esq = x.dir

        if x.dir != self.NIL:
            x.dir.pai = y

        x.pai = y.pai

        if y.pai is None:
            self.raiz = x

        elif y == y.pai.dir:
            y.pai.dir = x

        else:
            y.pai.esq = x

        x.dir = y
        y.pai = x

    def inserir(self, chave):
        novo = No(chave)
        novo.esq = novo.dir = self.NIL

        pai = None
        atual = self.raiz

        while atual != self.NIL:
            pai = atual

            if chave < atual.chave:
                atual = atual.esq
            else:
                atual = atual.dir

        novo.pai = pai

        if pai is None:
            self.raiz = novo

        elif chave < pai.chave:
            pai.esq = novo

        else:
            pai.dir = novo

        self._corrigir_insercao(novo)

    def _corrigir_insercao(self, z):
        while z.pai and z.pai.cor == RED:

            avo = z.pai.pai

            if z.pai == avo.esq:

                tio = avo.dir

                if tio.cor == RED:
                    z.pai.cor = BLACK
                    tio.cor = BLACK
                    avo.cor = RED
                    z = avo

                else:
                    if z == z.pai.dir:
                        z = z.pai
                        self._rot_esq(z)

                    z.pai.cor = BLACK
                    avo.cor = RED
                    self._rot_dir(avo)

            else:

                tio = avo.esq

                if tio.cor == RED:
                    z.pai.cor = BLACK
                    tio.cor = BLACK
                    avo.cor = RED
                    z = avo

                else:
                    if z == z.pai.esq:
                        z = z.pai
                        self._rot_dir(z)

                    z.pai.cor = BLACK
                    avo.cor = RED
                    self._rot_esq(avo)

        self.raiz.cor = BLACK


def montar_grafo(
    no,
    NIL,
    grafo,
    pos,
    cores,
    x=0,
    y=0,
    distancia=6
):
    if no == NIL:
        return

    grafo.add_node(no.chave)
    pos[no.chave] = (x, y)

    cores[no.chave] = (
        "red" if no.cor == RED else "black"
    )

    if no.esq != NIL:
        grafo.add_edge(no.chave, no.esq.chave)

        montar_grafo(
            no.esq,
            NIL,
            grafo,
            pos,
            cores,
            x - distancia,
            y - 1,
            distancia / 2
        )

    if no.dir != NIL:
        grafo.add_edge(no.chave, no.dir.chave)

        montar_grafo(
            no.dir,
            NIL,
            grafo,
            pos,
            cores,
            x + distancia,
            y - 1,
            distancia / 2
        )


valores = [
    40, 20, 60,
    10, 30, 50, 70,
    5, 15, 25, 35, 45
]

arvore = ArvoreRubroNegra()

for chave in valores:
    arvore.inserir(chave)


grafo = nx.DiGraph()
pos = {}
cores = {}

montar_grafo(
    arvore.raiz,
    arvore.NIL,
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

plt.title("Questão 6 - Escalonador - Rubro-Negra")
plt.show()