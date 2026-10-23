# Árvores Balanceadas

Este projeto foi feito para resolver 6 questões sobre **Árvore AVL** e **Árvore Rubro-Negra**.

Os códigos foram feitos em Python e usam as bibliotecas `networkx` e `matplotlib` para mostrar a árvore na tela.

## Instalação

```bash
pip install matplotlib networkx
```

## Questão 1 — AVL

Valores:

```text
10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150
```

**Resposta: AVL**

Escolhi AVL porque nessa situação acontecem muitas buscas e poucas inserções.

A AVL mantém a árvore mais balanceada, ajudando nas consultas.

A árvore fica assim:

```text
              80
           /      \
         40        120
        /  \       /  \
      20   60    100  140
     / \   / \   / \   / \
   10 30 50 70 90 110 130 150
```

---

## Questão 2 — Rubro-Negra

Valores:

```text
5, 10, 15, 20, 25, 30, 35, 40, 45, 50
```

**Resposta: Rubro-Negra**

Escolhi Rubro-Negra porque o sistema faz muitas inserções.

Ela consegue manter a árvore balanceada sem precisar fazer tantas mudanças na estrutura.

No código, os nós também aparecem nas cores vermelho e preto.

---

## Questão 3 — AVL

Valores:

```text
50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 65
```

**Resposta: AVL**

Escolhi AVL porque depois que a árvore é criada ela vai ser consultada muitas vezes.

Como a AVL mantém a árvore bem balanceada, as buscas ficam mais rápidas.

A árvore fica assim:

```text
          50
        /    \
      30      70
     /  \    /  \
   20   40  60  80
  / \   /   / \
10 25 35   55 65
```

---

## Questão 4 — Rubro-Negra

Valores:

```text
42, 17, 63, 9, 28, 55, 74, 3, 21, 38, 50, 70
```

**Resposta: Rubro-Negra**

Escolhi Rubro-Negra porque existem muitas inserções e remoções de sessões.

Como os dados mudam bastante, essa árvore é mais indicada para esse tipo de situação.

---

## Questão 5 — AVL

Valores:

```text
1, 2, 3, 4, 5, 6, 7
```

**Resposta: AVL**

Escolhi AVL porque os valores chegam em ordem crescente.

Sem balanceamento, a árvore poderia ficar parecida com uma lista.

Com a AVL, ela fica balanceada assim:

```text
        4
      /   \
     2     6
    / \   / \
   1   3 5   7
```

Isso deixa a busca mais rápida.

---

## Questão 6 — Rubro-Negra

Valores:

```text
40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45
```

**Resposta: Rubro-Negra**

Escolhi Rubro-Negra porque o sistema faz muitas alterações por segundo.

Como existem muitas inserções e mudanças na árvore, a Rubro-Negra é mais indicada para esse caso.