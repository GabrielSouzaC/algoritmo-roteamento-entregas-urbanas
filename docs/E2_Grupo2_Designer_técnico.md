# E2 — Design Técnico, Arquitetura e Backlog

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 13 de abril de 2026  
> **Peso:** 20% da nota final  

---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do projeto | Algoritmo de Roteamento para Entregas Urbanas |
| Repositório GitHub | |
| Integrante 1 | Gabriel Souza de Carvalho — 38598272 |
| Integrante 2 | Pedro Henrique dos Santos — 38898381 |
| Integrante 3 | Carlos Eduardo Laera Prado — 38070715 |

---

## 1. Algoritmos Escolhidos

### 1.1 Algoritmo Principal

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Dijkstra |
| Categoria | guloso / caminho mínimo em grafos |
| Complexidade de tempo | O((V + E) log V) |
| Complexidade de espaço | O(V) |
| Problema que resolve | Cálculo do caminho de menor tempo estimado entre dois vértices em um grafo ponderado com pesos não negativos |

**Por que este algoritmo foi escolhido?**

O algoritmo de Dijkstra foi escolhido por ser adequado para o problema definido no projeto, que consiste em encontrar o caminho de menor tempo estimado entre um depósito e um cliente em um grafo abstrato ponderado. Como os pesos das arestas representam tempo de deslocamento, e portanto são sempre não negativos, o Dijkstra se aplica de forma direta e eficiente.

Além disso, o algoritmo apresenta boa performance para grafos esparsos, especialmente quando implementado com fila de prioridade, o que é compatível com o cenário proposto de 20 a 50 vértices. Sua abordagem gulosa permite calcular incrementalmente o menor custo até cada vértice, garantindo a obtenção do caminho mínimo entre origem e destino.

Outro fator relevante é a capacidade de reconstruir o caminho percorrido, permitindo não apenas calcular o tempo total, mas também exibir a sequência de vértices, conforme definido nos objetivos do projeto.

**Alternativa descartada e motivo:**

| Algoritmo alternativo | Motivo da exclusão |
|----------------------|-------------------|
| Bellman-Ford | Embora resolva o problema de caminho mínimo e suporte pesos negativos, apresenta maior complexidade de tempo (O(V·E)), sendo menos eficiente que o Dijkstra no contexto do projeto, onde todos os pesos são não negativos.

**Limitações no contexto do problema:**

O algoritmo de Dijkstra não suporta grafos com pesos negativos, o que limita sua aplicação a cenários em que todos os custos são não negativos. No contexto deste projeto, essa limitação não impacta a solução, pois o tempo de deslocamento entre pontos não pode assumir valores negativos.

**Referência bibliográfica:**

CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. Algoritmos: teoria e prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

---

### 1.2 Algoritmo Adicional *(se houver)*

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | Bellman-Ford |
| Categoria | programação dinâmica / caminho mínimo em grafos |
| Complexidade de tempo | O(V · E) |
| Complexidade de espaço | O(V) |

**Justificativa:**

O algoritmo de Bellman-Ford foi considerado como alternativa complementar ao Dijkstra por também resolver o problema de caminho mínimo em grafos ponderados. Sua principal vantagem é a capacidade de lidar com pesos negativos, o que o torna mais geral em comparação ao Dijkstra.

No entanto, no contexto deste projeto, os pesos representam tempo de deslocamento e são sempre não negativos, tornando essa vantagem desnecessária. Além disso, o Bellman-Ford apresenta maior custo computacional, com complexidade de tempo O(V·E), sendo menos eficiente para o cenário proposto.

Apesar disso, sua inclusão como algoritmo adicional contribui para a análise comparativa, permitindo evidenciar por que o Dijkstra é mais adequado ao problema definido.

**Referência bibliográfica:**

> CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. Algoritmos: teoria e prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

---

## 2. Arquitetura em Camadas

> Insira o diagrama abaixo. Pode ser exportado do Draw.io, Excalidraw, etc.

![Diagrama de arquitetura](./docs/arquitetura_e2.png)

### Descrição das camadas

| Camada | Responsabilidade | Artefatos principais |
|--------|-----------------|----------------------|
| Apresentação (UI/CLI) | Receber a interação do usuário, permitindo selecionar o arquivo de entrada, informar origem e destino e visualizar o resultado do cálculo. | main_window.py, componentes de interface, formulários de entrada e painel de exibição do resultado |
| Aplicação (Service) | Orquestrar o fluxo do sistema, validando entradas, acionando a leitura do arquivo, chamando o algoritmo e retornando o resultado para a interface. | route_service.py, validadores de entrada, controladores de fluxo |
| Domínio (Core) | Implementar a lógica central do sistema, incluindo a estrutura do grafo, o algoritmo de Dijkstra e a reconstrução do caminho mínimo. | graph.py, vertex.py, edge.py, dijkstra.py |
| Infraestrutura (I/O) | Ler arquivos JSON e converter os dados de entrada para estruturas utilizadas pela camada de domínio. | json_reader.py, parser de entrada, carregador de dataset |

---

## 3. Estrutura de Diretórios

```
Algoritmo de Roteamento para Entregas Urbanas/
├── docs/
│   ├── README.md
│   ├── E1_template.md
│   └── E2_template.md
├── src/
│   ├── ui/
│   │   └── main_window.py
│   ├── service/
│   │   └── route_service.py
│   ├── core/
│   │   ├── graph.py
│   │   ├── vertex.py
│   │   └── edge.py
│   ├── algorithms/
│   │   ├── dijkstra.py
│   │   └── bellman_ford.py
│   ├── io/
│   │   └── json_reader.py
│   └── main.py
├── tests/
│   ├── test_graph.py
│   ├── test_dijkstra.py
│   └── test_json_reader.py
├── data/
│   ├── sample_graph.json
│   └── generated_graphs/
└── requirements.txt

```

> **Justificativa de desvios** *(se houver)*: 

A estrutura proposta segue o modelo sugerido no template, com pequenas adaptações para refletir a arquitetura em camadas definida no projeto. Foram adicionadas as pastas ui/ e service/ para representar explicitamente as camadas de apresentação e aplicação, garantindo a separação entre interface, orquestração e lógica de domínio. Além disso, a pasta algorithms/ foi mantida para isolar as implementações dos algoritmos de caminho mínimo das estruturas centrais do grafo.

---

## 4. Definição do Dataset

**Formato de entrada aceito:**

O sistema aceita arquivos no formato JSON, representando um grafo direcionado e ponderado. O arquivo contém a lista de vértices e as arestas, sendo cada aresta definida por um vértice de origem, um vértice de destino e um peso associado ao tempo estimado de deslocamento.

**Exemplo de estrutura do arquivo de entrada:**

```json
{
  "vertices": ["D", "C1", "C2", "C3", "C4", "C5", "C6"],
  "arestas": [
    { "origem": "D", "destino": "C1", "peso": 10 },
    { "origem": "D", "destino": "C2", "peso": 15 },
    { "origem": "C1", "destino": "C3", "peso": 12 },
    { "origem": "C1", "destino": "C4", "peso": 10 },
    { "origem": "C2", "destino": "C4", "peso": 5 },
    { "origem": "C2", "destino": "C5", "peso": 20 },
    { "origem": "C3", "destino": "C6", "peso": 8 },
    { "origem": "C4", "destino": "C6", "peso": 7 },
    { "origem": "C5", "destino": "C6", "peso": 25 }
  ]
}
```

**Estratégia de geração aleatória:**

| Parâmetro | Descrição |
|-----------|-----------|
| Número de vértices | Definido pelo usuário, variando entre 20 e 50 vértices |
| Densidade | Percentual de conexões entre os vértices, variando entre 0.2 e 0.6 |
| Faixa de pesos | Valores inteiros positivos representando tempo de deslocamento, entre 1 e 30 unidades |

---

## 5. Backlog do Projeto

### 5.1 In-Scope — O que será implementado

| # | Funcionalidade | Prioridade | Critério de aceite |
|---|---------------|------------|-------------------|
| 1 | Leitura de arquivo JSON | Alta | Dado um arquivo JSON válido contendo vértices e arestas, quando o usuário carregar o arquivo na interface, então o sistema deve importar os dados sem erros |
| 2 | Construção do grafo | Alta | Dado um conjunto de dados carregado, quando o sistema processar o arquivo, então deve construir corretamente a estrutura de grafo com todos os vértices e arestas |
| 3 | Execução do algoritmo de Dijkstra | Alta | Dado um grafo válido e um vértice de origem e destino, quando o algoritmo for executado, então o sistema deve calcular o caminho de menor tempo estimado corretamente |
| 4 | Exibição do resultado na interface | Média | Dado um cálculo concluído, quando o algoritmo retornar o resultado, então o sistema deve exibir o caminho mínimo e o tempo total na interface |
| 5 | Validação de entrada do usuário | Média | Dado um arquivo inválido ou vértices inexistentes, quando o usuário tentar executar o cálculo, então o sistema deve exibir uma mensagem de erro apropriada |

### 5.2 Out-of-Scope — O que NÃO será feito

| Funcionalidade excluída | Motivo |
|------------------------|--------|
| Implementação do algoritmo Bellman-Ford | Utilizado apenas para comparação teórica, não sendo necessário para o problema com pesos não negativos |
| Interface web ou mobile | Fora do escopo do projeto, que foca em uma aplicação local com interface simples |
| Otimização de múltiplas rotas (TSP) | Problema mais complexo e não alinhado com o escopo definido de caminho mínimo entre dois pontos |

---

## Checklist de Entrega

- [x] Big-O de tempo e espaço declarados para cada algoritmo
- [x] Ao menos 1 alternativa descartada com justificativa
- [x] Diagrama de arquitetura com 4 camadas identificadas
- [x] Referência bibliográfica para cada algoritmo (ABNT ou IEEE)
- [x] Backlog com ≥ 5 itens In-Scope e ≥ 3 Out-of-Scope
- [x] Ao menos 3 critérios de aceite no formato "dado / quando / então"
- [x] Exemplo de estrutura de arquivo de entrada presente

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
