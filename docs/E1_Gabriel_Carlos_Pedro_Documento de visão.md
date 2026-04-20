# E1 — Proposta e Definição do Projeto

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 25 de março de 2026  
> **Peso:** 10% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Algoritmo de Roteamento para Entregas Urbanas |
| Integrante 1 | Gabriel Souza de Carvalho — 38598272 |
| Integrante 2 | Pedro Henrique dos Santos — 38898381 |
| Integrante 3 | Carlos Eduardo Laera Prado — 38070715 |
| Domínio de aplicação | logística, roteamento e navegação urbana |

---

## 1. Contexto e Motivação

> Descreva o problema do mundo real que será abordado. Por que ele é relevante?  
> *Orientação: 2 a 3 parágrafos. Seja específico — evite generalizações.*

O projeto aborda o problema de encontrar a rota de menor tempo estimado entre um depósito e um cliente em um cenário de entregas urbanas. Em operações logísticas, a definição de trajetos influencia diretamente o prazo das entregas, o custo operacional e a organização do processo. Embora existam ferramentas de navegação consolidadas, a proposta deste trabalho não é reproduzir um sistema completo de mapas urbanos, mas estudar como a Teoria dos Grafos pode ser aplicada ao cálculo de caminhos mínimos em um contexto viável.

A motivação do projeto surgiu de uma experiência prática no ambiente de trabalho, no qual já existe o uso de uma API de rotas para apoiar deslocamentos. No entanto, neste projeto, a API não será substituída, sendo utilizada apenas como referência de comparação. A proposta central é construir uma solução própria baseada em grafos, capaz de representar um conjunto limitado de pontos de entrega e calcular o trajeto de menor tempo.

Para tornar o escopo executável, o problema será modelado como um grafo abstrato inspirado em um cenário de logística, com aproximadamente 20 a 50 vértices representando o depósito e os clientes. As conexões terão pesos associados ao tempo estimado de deslocamento. Assim, o projeto transforma uma situação real em um problema computacional bem definido, permitindo analisar algoritmos de caminho mínimo e comparar seus resultados com os de uma API.

---

## 2. Objetivo Geral

> O que o sistema deve ser capaz de fazer ao final?  
> *Orientação: 1 frase clara e objetiva. Ex.: "O sistema deve calcular a rota de menor custo entre dois pontos em um mapa urbano."*

O sistema deve ser capaz de calcular o caminho de menor tempo estimado entre dois pontos (depósito e cliente) em um grafo abstrato ponderado, utilizando o algoritmo de Dijkstra.

---

## 3. Objetivos Específicos

> Desmembre o objetivo geral em metas mensuráveis.  
> *Orientação: liste entre 3 e 5 itens. Cada item deve ser verificável — use verbos como "implementar", "calcular", "exibir", "carregar".*

- [ ] Implementar a representação do problema como um grafo abstrato ponderado, no qual os vértices representam o depósito e os clientes, e as arestas representam as conexões entre esses pontos.
- [ ] Definir os pesos das arestas com base no tempo estimado de deslocamento entre os vértices.
- [ ] Implementar o algoritmo de Dijkstra para calcular o caminho de menor tempo estimado entre dois vértices do grafo.
- [ ] Desenvolver a lógica para receber como entrada os pontos de origem e destino no grafo.
- [ ] Exibir o caminho mínimo encontrado, indicando a sequência de vértices percorridos e o tempo total estimado.

---

## 4. Público-Alvo / Caso de Uso Principal

> Para quem ou em qual cenário o sistema seria utilizado?  
> *Orientação: descreva um cenário concreto de uso. Ex.: "Um entregador de aplicativo que precisa otimizar a sequência de entregas em um bairro."*

O sistema é voltado para um operador logístico responsável pelo planejamento de entregas em um cenário inspirado em operações reais. Nesse contexto, o operador define o trajeto entre um ponto de origem (depósito) e um destino (cliente), buscando minimizar o tempo de deslocamento.

O usuário informa os pontos no sistema, que utiliza a modelagem em grafo para calcular o caminho de menor tempo estimado. Esse processo pode ser repetido para diferentes entregas, auxiliando na decisão sobre quais rotas adotar.

Assim, o sistema atua como ferramenta de apoio ao planejamento logístico, permitindo avaliar rotas individuais de forma estruturada, sem a necessidade de resolver múltiplos destinos simultaneamente.

---

## 5. Justificativa Técnica — Por que Grafos?

> Por que a modelagem em grafo é a abordagem mais adequada para este problema?  
> *Orientação: explique quais elementos do problema mapeiam naturalmente para vértices e arestas. Mencione se há pesos, direção, ou restrições que reforçam a escolha.*

A modelagem em grafos é adequada para este problema, pois permite representar explicitamente as relações entre os pontos de entrega e aplicar algoritmos eficientes de caminhos mínimos. Neste projeto, os vértices representam o depósito e os clientes, enquanto as arestas representam conexões com pesos associados ao tempo estimado.

Diferentemente de abordagens simples, como matrizes de distância ou listas de pares origem-destino, o grafo permite explorar múltiplos caminhos entre vértices. Isso é essencial para algoritmos como o de Dijkstra, que percorre vizinhos e atualiza custos de forma eficiente.

Além disso, grafos oferecem flexibilidade para extensões, como inclusão de restrições ou alteração de pesos. Em contraste, representações não estruturadas exigiriam reprocessamento completo ou não permitiriam o uso direto de algoritmos clássicos.

Portanto, a escolha por grafos se justifica por viabilizar o uso de algoritmos consolidados de caminho mínimo, garantindo uma solução eficiente e adequada ao escopo.

---

## 6. Tipo de Grafo

> Especifique as características do grafo que o problema requer.

| Característica                   | Escolha                               | Justificativa breve                                                                                                                                                                                                |
| -------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Dirigido ou não-dirigido         | Dirigido                              | As conexões entre os pontos podem representar rotas com restrições de sentido, onde o tempo de deslocamento de A para B pode diferir do percurso inverso.                                                          |
| Ponderado ou não-ponderado       | Ponderado                             | Cada aresta possui um peso associado ao tempo estimado de deslocamento entre os vértices, que é o critério utilizado no cálculo do caminho mínimo.                                                                 |
| Conectado / bipartido / geral    | Geral (não necessariamente conectado) | O grafo representa um conjunto de pontos de entrega que podem não estar totalmente conectados. O sistema deve ser capaz de identificar quando não há caminho entre dois vértices e tratar esse caso adequadamente. |
| Representação interna pretendida | Lista de adjacência                   | Estrutura eficiente para grafos esparsos, permitindo armazenar apenas conexões existentes e facilitando a execução do algoritmo de Dijkstra.                                                                       |


---

## 7. Diagrama Conceitual

> Insira aqui ao menos uma figura que ilustre o domínio do problema.  
> *Pode ser uma imagem exportada do Draw.io, Excalidraw, foto de esboço à mão etc.*  

A figura correspondente ao diagrama foi entregue em arquivo separado, conforme as orientações da disciplina.

**Legenda:** A figura representa o problema modelado como um grafo abstrato dirigido e ponderado, no qual os vértices correspondem ao depósito (D) e aos clientes (C1 a C6), enquanto as arestas representam as possíveis conexões entre esses pontos, com pesos associados ao tempo estimado de deslocamento (em minutos). As setas indicam a direção das rotas, permitindo representar diferenças no tempo conforme o sentido do percurso. O diagrama ilustra múltiplos caminhos possíveis entre a origem (D) e o destino (C6), sendo destacado o caminho de menor tempo estimado, evidenciando a aplicação do algoritmo de Dijkstra para a determinação da rota ótima dentro do grafo.
---

## Checklist de Entrega

Antes de submeter, confirme:

- [X] Texto entre 300 e 600 palavras (seções 1 a 5)
- [X] Todos os campos da tabela de identificação preenchidos
- [X] Tipo de grafo especificado com justificativa
- [X] Diagrama presente e referenciado no texto
- [X] Arquivo nomeado como `E1_NomeGrupo_Grafos.docx` (versão Word) ou PR aberto (versão GitHub)

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
