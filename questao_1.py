import networkx as nx
import matplotlib.pyplot as plt


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class AVL:
    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def atualizar_altura(self, no):
        no.altura = 1 + max(
            self.altura(no.esquerda),
            self.altura(no.direita)
        )

    def rotacao_direita(self, y):
        x = y.esquerda
        t2 = x.direita

        x.direita = y
        y.esquerda = t2

        self.atualizar_altura(y)
        self.atualizar_altura(x)

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        t2 = y.esquerda

        y.esquerda = x
        x.direita = t2

        self.atualizar_altura(x)
        self.atualizar_altura(y)

        return y

    def inserir(self, raiz, valor):
        if raiz is None:
            return No(valor)

        if valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)

        elif valor > raiz.valor:
            raiz.direita = self.inserir(raiz.direita, valor)

        else:
            return raiz

        self.atualizar_altura(raiz)

        balanceamento = (
            self.altura(raiz.esquerda)
            - self.altura(raiz.direita)
        )

        # Caso esquerda-esquerda
        if balanceamento > 1 and valor < raiz.esquerda.valor:
            return self.rotacao_direita(raiz)

        # Caso direita-direita
        if balanceamento < -1 and valor > raiz.direita.valor:
            return self.rotacao_esquerda(raiz)

        # Caso esquerda-direita
        if balanceamento > 1 and valor > raiz.esquerda.valor:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Caso direita-esquerda
        if balanceamento < -1 and valor < raiz.direita.valor:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz


def montar_grafo(no, grafo, pos, x=0, y=0, distancia=8):

    if no is None:
        return

    grafo.add_node(no.valor)
    pos[no.valor] = (x, y)

    if no.esquerda is not None:
        grafo.add_edge(no.valor, no.esquerda.valor)

        montar_grafo(
            no.esquerda,
            grafo,
            pos,
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
            x + distancia,
            y - 1,
            distancia / 2
        )


# Questão 1
valores = [
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100,
    110, 120, 130, 140, 150
]

arvore = AVL()
raiz = None

for valor in valores:
    raiz = arvore.inserir(raiz, valor)


grafo = nx.DiGraph()
pos = {}

montar_grafo(
    raiz,
    grafo,
    pos
)


plt.figure(figsize=(12, 7))

nx.draw(
    grafo,
    pos,
    with_labels=True,
    node_size=1800,
    font_size=10,
    font_weight="bold",
    arrows=False
)

plt.title(
    "Questão 1 - Catálogo de Produtos - Árvore AVL"
)

plt.show()