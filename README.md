# Árvores Balanceadas

Este projeto contém a resolução de 6 questões usando **Árvore AVL** e **Árvore Rubro-Negra**.

Os códigos foram feitos em Python com base nas aulas de AVL e Rubro-Negra.

Para mostrar as árvores, foram usadas as bibliotecas:

```bash
pip install matplotlib networkx
```

## Questão 1 — AVL

Valores:

```text
10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150
```

**Resposta: AVL**

A AVL foi escolhida porque o sistema realiza muitas buscas e poucas inserções.

Como os valores chegam em ordem crescente, uma árvore comum poderia ficar desbalanceada.

A AVL usa o fator de balanceamento e rotações para manter a árvore equilibrada.

Na aula, o fator de balanceamento é calculado por:

```text
FB = altura(direita) - altura(esquerda)
```

A árvore final fica balanceada mesmo com os valores inseridos em ordem crescente.

---

## Questão 2 — Rubro-Negra

Valores:

```text
5, 10, 15, 20, 25, 30, 35, 40, 45, 50
```

**Resposta: Rubro-Negra**

Foi escolhida porque o sistema realiza muitas inserções.

Na Rubro-Negra, cada novo nó nasce vermelho e a árvore realiza recolorações ou rotações quando necessário.

A raiz sempre termina preta.

---

## Questão 3 — AVL

Valores:

```text
50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 65
```

**Resposta: AVL**

A AVL foi escolhida porque depois da criação da árvore existem muitas consultas.

Como a AVL mantém a árvore bem balanceada, as buscas continuam eficientes.

A aula mostra que a AVL mantém o fator de balanceamento de todos os nós entre:

```text
-1, 0 e +1
```



---

## Questão 4 — Rubro-Negra

Valores:

```text
42, 17, 63, 9, 28, 55, 74, 3, 21, 38, 50, 70
```

**Resposta: Rubro-Negra**

Foi escolhida porque existem muitas inserções e remoções de sessões.

A Rubro-Negra é indicada para estruturas que sofrem muitas alterações.

Ela usa as cores dos nós para controlar o balanceamento.

O nó possui:

```text
chave
cor
esq
dir
pai
```



---

## Questão 5 — AVL

Valores:

```text
1, 2, 3, 4, 5, 6, 7
```

**Resposta: AVL**

Os valores chegam completamente ordenados.

Em uma árvore comum, isso poderia formar uma estrutura parecida com uma lista.

A AVL realiza rotações automaticamente e mantém a árvore balanceada.

Essa mesma sequência aparece como exercício na aula de AVL.

A árvore final fica:

```text
        4
      /   \
     2     6
    / \   / \
   1   3 5   7
```

---

## Questão 6 — Rubro-Negra

Valores:

```text
40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45
```

**Resposta: Rubro-Negra**

Foi escolhida porque o sistema realiza muitas alterações por segundo.

A Rubro-Negra trabalha bem com muitas inserções porque seu balanceamento é menos rígido que o da AVL.

Durante a inserção:

```text
Pai preto
→ nenhuma correção

Pai vermelho + tio vermelho
→ recoloração

Pai vermelho + tio preto
→ rotação
```



---

## Visualização

As árvores são exibidas usando:

```python
import networkx as nx
import matplotlib.pyplot as plt
```

O `networkx` monta a estrutura da árvore e o `matplotlib` mostra o resultado na tela.

Os códigos não usam `print()` para mostrar a árvore e não criam arquivos PNG.

A visualização é aberta com:

```python
plt.show()
```

Nas árvores Rubro-Negra:

- vermelho representa um nó rubro;
- preto representa um nó negro.

Nas árvores AVL, os nós são reorganizados automaticamente através das rotações LL, RR, LR e RL.