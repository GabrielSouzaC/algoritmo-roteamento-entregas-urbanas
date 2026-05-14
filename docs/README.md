# Algoritmo de Roteamento para Entregas Urbanas

**Projeto Final - Teoria dos Grafos**

Sistema que calcula o **caminho de menor tempo estimado** entre dois pontos (depósito e cliente) em um grafo abstrato dirigido e ponderado, utilizando o algoritmo de **Dijkstra**.

## Integrantes

- Gabriel Souza de Carvalho — 38598272
- Pedro Henrique dos Santos — 38898381
- Carlos Eduardo Laera Prado — 38070715

## Descrição

O projeto modela um problema de logística urbana como um grafo abstrato, onde:
- **Vértices** representam o Depósito (`D`) e Clientes (`C1`, `C2`, ...).
- **Arestas** representam rotas possíveis com pesos correspondentes ao **tempo estimado** de deslocamento.
- O objetivo é encontrar a rota de menor tempo entre dois pontos.

## Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/GabrielSouzaC/algoritmo-roteamento-entregas-urbanas.git

# 2. Entre na pasta do projeto
cd algoritmo-roteamento-entregas-urbanas

# 3. Execute o programa
python src/main.py
```