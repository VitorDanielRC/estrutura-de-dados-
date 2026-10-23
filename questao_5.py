import networkx as nx
import matplotlib.pyplot as plt


class No:
    def __init__(self, v):
        self.valor = v
        self.esquerda = None
        self.direita = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None

    def _h(self, no):
        return no.altura if no else 0

    def _fb(self, no):
        return self._h(no.direita) - self._h(no.esquerda)

    def _atualiza_altura(self, no):
        no.altura = 1 + max(
            self._h(no.esquerda),
            self._h(no.direita)
        )

    def _rotacao_direita(self, y):
        x = y.esquerda

        y.esquerda = x.direita
        x.direita = y

        self._atualiza_altura(y)
        self._atualiza_altura(x)

        return x

    def _rotacao_esquerda(self, x):
        y = x.direita

        x.direita = y.esquerda
        y.esquerda = x

        self._atualiza_altura(x)
        self._atualiza_altura(y)

        return y

    def inserir(self, v):
        self.raiz = self._inserir(self.raiz, v)

    def _inserir(self, no, v):
        if no is None:
            return No(v)

        if v < no.valor:
            no.esquerda = self._inserir(no.esquerda, v)

        elif v > no.valor:
            no.direita = self._inserir(no.direita, v)

        else:
            return no

        self._atualiza_altura(no)

        fb = self._fb(no)

        if fb < -1 and v < no.esquerda.valor:
            return self._rotacao_direita(no)

        if fb > 1 and v > no.direita.valor:
            return self._rotacao_esquerda(no)

        if fb < -1 and v > no.esquerda.valor:
            no.esquerda = self._rotacao_esquerda(
                no.esquerda
            )
            return self._rotacao_direita(no)

        if fb > 1 and v < no.direita.valor:
            no.direita = self._rotacao_direita(
                no.direita
            )
            return self._rotacao_esquerda(no)

        return no


def montar_grafo(no, grafo, pos, x=0, y=0, distancia=4):
    if no is None:
        return

    grafo.add_node(no.valor)
    pos[no.valor] = (x, y)

    if no.esquerda:
        grafo.add_edge(no.valor, no.esquerda.valor)

        montar_grafo(
            no.esquerda,
            grafo,
            pos,
            x - distancia,
            y - 1,
            distancia / 2
        )

    if no.direita:
        grafo.add_edge(no.valor, no.direita.valor)

        montar_grafo(
            no.direita,
            grafo,
            pos,
            x + distancia,
            y - 1,
            distancia / 2
        )


valores = [
    1, 2, 3, 4, 5, 6, 7
]

arvore = AVL()

for v in valores:
    arvore.inserir(v)


grafo = nx.DiGraph()
pos = {}

montar_grafo(
    arvore.raiz,
    grafo,
    pos
)

plt.figure(figsize=(10, 6))

nx.draw(
    grafo,
    pos,
    with_labels=True,
    node_size=1800,
    font_size=11,
    font_weight="bold",
    arrows=False
)

plt.title("Questão 5 - Cadastro Ordenado - AVL")
plt.show()